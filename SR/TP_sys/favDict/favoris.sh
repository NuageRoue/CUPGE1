#!/bin/bash

FAV="$HOME/.favoris_bash"

touch "$FAV"

function already_in ()
{
	LINE=$( grep -wn "$1" "$FAV" | awk -F':' '{print $1}' ) # on récupère le numéro de la ligne (grep -n affiche ce numéro en première position, on le récupère avec awk, en précisant les ':' comme séparateur. 
	
	head -n $[ $LINE - "1" ] $FAV > .temp # on récupère les lignes précédentes
	echo "$1 -> $( pwd )" >> .temp #on ajoute notre ligne modifiée
	if [ $LINE -lt $( cat $FAV | wc -l ) ];then # on ajoute les lignes suivantes
		tail -n $[ "$( cat $FAV | wc -l )" - "$LINE" ] "$FAV" >> ".temp"
	fi
	rm $FAV
	mv .temp $FAV
	# on remplace fichier le fichier par le fichier temporaire
}


function S ()
{
	if [ "$#" -eq "1" ]; then # il faut en entrée un seul et unique argument
		if ! [[ $1 =~ " " ]];then #il ne doit pas comporter d'espace
			if grep -qw $1 "$FAV" ;then # si le favori existe deja
				echo -e "Le répertoire $(pwd) est sauvegardé dans vos favoris
	-> raccourci : $1"
				already_in $1 #on le regénère
			else
				echo -e "Le répertoire $(pwd) est sauvegardé dans vos favoris
        -> raccourci : $1"
				echo "$1 -> $( pwd )" >> $FAV # sinon on le redéfini
			fi
		else
			echo "attention : le nom de favori ne doit pas être composé d'espace"
		fi
	elif [ "$#" -lt "1" ]; then
		echo "attention: vous devez fournir un argument pour définir le nom du favori"
	else
		echo "attention: vous ne devez fournir qu'un seul argument SANS ESPACES pour définir le nom du favori"
	fi
}

function R () {
	
	if [ $# -gt "0" ]; then
		LINE_NUMB=1
                SEP=" "
		touch ".temp"
                while [ $LINE_NUMB -le $( cat $FAV | wc -l ) ]; do #on parcourt toutes les lignes du fichier;
			if [[ " $@ " == " $(head -n $LINE_NUMB "$FAV" | tail -n 1 | awk '{ print $1 }') " ]]; then #si le favori fait parti des favoris a supprimer;
                                echo "le favori '$( head -n $LINE_NUMB $FAV | tail -n 1 | awk '{ print $1 }')' est supprimé de votre liste" #on indique qu'on supprime ce favori
                        else #sinon (=> il doit etre gardee)
                                head -n $LINE_NUMB "$FAV" | tail -n 1 >> ".temp" #on l'ajoute au fichier .temp
                        fi
                        LINE_NUMB=$[ $LINE_NUMB + 1 ] #on incremente le compteur de ligne
                done
                rm $FAV
                mv ".temp" $FAV # on remplace notre fichier par le fichier temporaire
	else
		echo "attention: il faut fournir un ou plusieurs alias à supprimer"
	fi
}


function C () 
{
	if [ "$#" -eq "1" ];then
		#echo $(grep $1 "$FAV")
		if grep -qw $1 "$FAV" ;then # si le mot est présent en tant que mot complet :
			cd $(echo $(grep -w $1 "$FAV") | awk '{ print $3 }') # on se déplace dans le dossier associé avec awk qui récupère le chemin de ce dossier
			echo "Vous êtes maintenant dans le répertoire $(pwd)."
		elif [ $(grep -c $1 "$FAV") -eq "1" ];then # si il est présent dans un seul alias :
			cd $(echo $(grep $1 "$FAV") | awk '{ print $3 }') # idem
			echo "Vous êtes maintenant dans le répertoire $(pwd)."
		elif [ $(grep -c $1 "$FAV") -gt 1 ];then # si plusieurs favoris contiennent notre demande, on l'indique et on ne fait rien
			echo "il y a plusieurs favoris contenant '$1' :"
			grep $1 "$FAV" | awk '{ print $1 }'
		else
			echo "le favori '$1' n'existe pas"
		fi
	else
		echo "attention: cette commande nécessite en entrée un seul argument qui soit un alias enregistré."
	fi
}

function L ()
{
	if [ -f $FAV ]; then
		if [ $( cat $FAV | wc -l ) -gt 0 ]; then
			cat $FAV # on liste les favoris existants
		else
			echo "attention, la liste de favoris est vide"
		fi
	else
		echo "attention: la liste de favoris a été supprimée"
	fi
}
