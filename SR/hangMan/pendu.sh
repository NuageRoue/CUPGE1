#!/bin/bash

# variables utiles :

DICT=$1
MOT_A_TROUVER=""
MOT_DEVINE=""
LETTRES_RESTANTES="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
LETTRES_TESTEES=""
NB_TENTATIVES=0

function update_word () {
	# fonction qui "met à jour" le mot deviné en parcourant le mot à trouver charactère par charactère. Si le charactère est dans la chaine des lettres testées, on l'affiche. Sinon, on met un underscore '_'

	MOT_DEVINE=""
	for i in $(seq 1 ${#MOT_A_TROUVER}); do #on parcours la chaine
		if [[ $LETTRES_TESTEES =~ $(echo $MOT_A_TROUVER | cut -c$i) ]];then # $(echo $MOT_A_TROUVER | cut -c$i) correspond au charactère courant
			MOT_DEVINE="$MOT_DEVINE""$(echo $MOT_A_TROUVER | cut -c$i)"
		else
			MOT_DEVINE="$MOT_DEVINE""_"
		fi	
	done

}

function choisi_mot () {
	# fonction choisissant un mot dans le fichier contenant les mots. 
	NB_WORD=$( cat $DICT | wc -l )
	WORD_LINE=$(shuf -i 1-$NB_WORD -n1) #on utilise shuf plutot que $RANDOM pour ne pas se cantonner aux 32767 premiers mots d'un hypothétique dictionnaire plus long
	MOT_A_TROUVER=$( head -n $WORD_LINE $DICT | tail -n 1) #on a donc genere un numero de ligne, on a plus qu'à combiner head et tail pour recuperer le mot associe
	update_word #on "met à jour" le mot deviné (on le remplit donc d'underscore comme aucun charactère n'a été proposé) 
}

function teste_lettre () {
	# fonction testant la lettre fournit en entree.
	LETTRES_RESTANTES=$(echo $LETTRES_RESTANTES | tr -d $1) #on met à jour les lettres restantes;
	if [[ $LETTRES_TESTEES =~ $1 ]];then #si elle fait parti des lettres testées, on l'indique et on ne fait rien de plus.
		echo "attention: vous avez déjà testé cette lettre;"
	else
		LETTRES_TESTEES="$LETTRES_TESTEES""$1" #sinon, on l'ajoute et on continue:
		if [[ $MOT_A_TROUVER =~ $1 ]];then #si elle fait parti du mot à deviner, on met à jour le mot deviné
			echo "le mot contient $1"
			update_word
		else
			echo "le mot ne contient pas $1" #sinon, on ajoute 1 au compteur d'erreur.
			NB_TENTATIVES=$[ $NB_TENTATIVES + 1]
		fi
	fi
}

#affichage lettres
function print_lettres () {
	# fonction affichant la chaine des lettres testees avec un espace entre chaque lettres
	OUTPUT=""
	for i in $(seq 1 ${#LETTRES_TESTEES}); do
		OUTPUT="$OUTPUT"$(echo $LETTRES_TESTEES | cut -c$i)" "
	done
	echo -e "$OUTPUT \n"
}

#affichage pendu
function affichage_pendu () {
	#fonction qui choisit quelle étape du pendu afficher
	case $NB_TENTATIVES in

0)
echo -e "\n\n\n\n\n\n\n"
;;
1)
echo -e "\n\n\n\n\n\n___ ___"
;;
2)
echo -e "\n   |   \n   |   \n   |   \n   |   \n   |   \n___|___"
;;
3)
echo -e "    _____\n   |   \n   |   \n   |   \n   |   \n   |   \n___|___"
;;
4)
echo -e "    _____\n   |     |\n   |   \n   |   \n   |   \n   |   \n___|___"
;;
5)
echo -e "    _____\n   |     |\n   |     0\n   |   \n   |   \n   |   \n___|___"
;;
6)
echo -e "    _____\n   |     |\n   |     0\n   |     |\n   |   \n   |   \n___|___"
;;
7)
echo -e "    _____\n   |     |\n   |     0\n   |    /|\n   |   \n   |   \n___|___"
;;
8)
echo -e "    _____\n   |     |\n   |     0\n   |    /|\\ \n   |   \n   |   \n___|___"
;;
9)
echo -e "    _____\n   |     |\n   |     0\n   |    /|\\ \n   |    /\n   |    \n___|___"
;;
10)
echo -e "    _____\n   |     |\n   |     0\n   |    /|\\ \n   |    / \\ \n   |    \n___|___"
;;

esac
}


function boucle_pendu () {
	# boucle principale
	if [ -f $DICT ]; then # on verifie que l'argument est bien un nom de fichier
		choisi_mot #si c'est le cas, on choisit un mot dans le fichier
		while [ $NB_TENTATIVES -lt 10 ] && ! [ $MOT_DEVINE == $MOT_A_TROUVER ];do # la boucle continue tant que le nombre de tentative n'atteint pas 10, ou que le mot n'est pas deviné
			affichage_pendu #on affiche le pendu (qui change selon le nombre d'erreurs)
			echo -e "\nLettres testées :\n"
			print_lettres #on affiche les lettres testées
			echo $MOT_DEVINE # et le mot deviné
			read -rep $'Choisissez une lettre : \n' LETTRE #on demande une lettre en entrée
			if [[ $LETTRE == [A-Z] ]];then # si la lettre est une majuscule :
				teste_lettre $LETTRE #on teste la lettre;
			elif [ $LETTRE == $MOT_A_TROUVER ];then # si la lettre fournie par l'utilisateur est le mot à trouver, on met à jour manuellement le mot deviné
				MOT_DEVINE=$LETTRE
			else
				if [ $LETTRE == ":q" ];then #si la lettre fournie par l'utilisateur est ":q"
					break # on sort de la boucle
				elif [ $(echo $LETTRE | tr -d '\n'| wc -c) -gt "1" ] && [[ $LETTRE =~ ^[A-Z]+$ ]];then # si on fournit plusieurs charactères et que ce n'est pas le mot à trouver;
					echo "le mot n'est pas $LETTRE !" # on indique que ce n'est pas le mot à trouver
					NB_TENTATIVES=$[ $NB_TENTATIVES + 1 ]
				else
					echo "attention: vous devez fournir en entrée une ou plusieurs lettres majuscules."
				fi
			fi
			echo -e "\n\n************************************************************************************************************************************************\n"
		done
		if [ $NB_TENTATIVES -eq 10 ]; then #si à lasortie de la boucle le nombre de tentatives erronées est égal à 10, alors le joueur a perdu.
			affichage_pendu
			echo -e "\n\nperdu :( \nLe mot était $MOT_A_TROUVER" 
		elif [ $MOT_DEVINE == $MOT_A_TROUVER ];then #si le mot deviné est le mot à trouver, alors le joueur a gagné.
			echo -e "\ngagné :) \nLe mot était bien $MOT_A_TROUVER !"
		elif [ $LETTRE == ":q" ]; then #si $LETTRE est égal à ":q" alors la boucle a été stoppé manuellement.
			echo "fin du jeu."
		fi
	else
		echo "attention : le fichier renseigné n'existe pas"
	fi
}

if [ "$#" -eq "1" ];then # pour exécuter, il faut fournir en entrée un nom de fichier
	boucle_pendu
else
	echo "attention: prière de renseigner en entrée un fichier contenant des mots;" #si on n'en fournit pas, on ne peut pas exécuter
fi
