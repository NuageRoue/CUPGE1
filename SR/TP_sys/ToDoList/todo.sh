#!/bin/bash

#Clement OLIVEIRA, CUPGE1

TACHES=$HOME/.todo_list

function todo ()
{
touch "$TACHES"

if [ "$#" -ge "1" ]; then #quoi qu'il arrive, on a besoin d'au moins un argument pour executer les differentes commandes;

#ajout dans la liste
#conditions requises : au moins 3 arguments dont le premier soit "add", le 2eme un numero (de ligne) et la suite soit une tache
if [ "$1" == "add" ] && [ "$#" -ge "3" ] && [[ $2 =~ ^[0-9]+$ ]] && [ "$2" != "0" ]; then 	
	head -n $[ $2 - 1 ] "$TACHES" > ".temp" #on cree un fichier qui contient l'ensemble des lignes precedant celle a laquelle on veut inscrire la tache
	echo ${@:3} >> ".temp" #on ajoute la tache sur la ligne souhaitee 
	if [ "$( cat $TACHES | wc -l )" -ge $2 ]; then #si cette ligne est deja occupee, alors il faut ajouter tout le contenu du fichier a partir de cette ligne : $( cat $TACHES | wc -l) correspond au nombre de ligne de la liste, donc si la ligne que l'on souhaite ajouter est occupee, alors elle sera inferieure ou egale a la dernière ligne.
		tail -n $[ "$( cat $TACHES | wc -l )" - "$2" + "1" ] "$TACHES" >> ".temp"
		echo "ajout de la tache ${@:3} sur la ligne $2"
	fi
	rm $TACHES
	mv ".temp" $TACHES #on remplace la liste par notre fichier temporaire (qui contient la liste et la nouvelel tache)

#gestion des erreurs liees a l'ajout d'une tache dans la liste:
elif [ "$1" == "add" ]; then
	if [ "$#" -lt "3" ]; then #s'il n'y a pas assez d'argument, alors la commande ne fonctionne pas
		echo "attention: pour ajouter dans la liste il faut utiliser la syntaxe suivante : 'todo add NUMERO_DE_LIGNE TACHE'"
	fi
	if [ "$#" -ge "2" ]; then
		if [[ ! "$2" =~ ^[0-9]+$ ]] || [ "$2" -eq "0" ] ; then #idem si on en a au moins 2 mais que le 2eme n'est pas un entier valide
		echo "attention: le 2eme argument doit etre un numero de ligne superieur a 0"
		fi
	fi




#suppression dans la liste
#conditions requises : au moins 2 arguments dont le premier soit "done" et les suivants des numeros de lignes
elif [ "$1" == "done" ] && [ $# -ge "2" ]; then
	touch ".temp" #on cree un fichier temporaire vide dans lequel on ajoutera les taches a garder
		LINE_NUMB=1
		SEP=" "
		while [ $LINE_NUMB -le $( cat $TACHES | wc -l ) ]; do #on parcourt toutes les lignes du fichier;
			if [[ " ${@:2} " =~ " ${LINE_NUMB} " ]]; then #si le numero de la ligne fait parti des lignes a supprimer;  
				echo "suppression de la tache $( head -n $LINE_NUMB $TACHES | tail -n 1 )" #on indique qu'on termine cette tache
			else #sinon (=> si cette tache doit etre gardee)
				head -n $LINE_NUMB "$TACHES" | tail -n 1 >> ".temp" #on l'ajoute au fichier .temp
			fi
			LINE_NUMB=$[ $LINE_NUMB + 1 ] #on incremente le compteur de ligne
		done
		rm $TACHES
		mv ".temp" $TACHES #on remplace la liste par le fichier temporaire (qui contient donc toutes les lignes que l'on veut garder)
#gestion des erreurs liees a cette commande :
elif [ "$1" == "done" ] && [ "$#" -le "1" ]; then #si on a pas au moins un argument, alors la commande ne s'execute pas
	echo "attention: il faut fournir des numeros de tache a conclure!"



#affichage du contenu de la liste de la liste
elif [ "$1" == "list" ] && [ $# == "1" ] && [ $( cat $TACHES | wc -l ) -gt "0" ]; then #conditions requises : un seul argument qui soit "list" et une liste de tache qui soit non vide
	nl -s" - " $TACHES #on affiche la liste avec la commande nl, qui prefixe chaque ligne par "n - ", n etant le numero de la ligne dans la liste;
#gestion des erreurs liees a cette commande :
elif [ "$1" == "list" ] && [ $# == "1" ]; then #si on arrive ici, c'est que la liste courante est vide : on ne doit rien afficher
	echo "la liste de tache est vide"



#commandes bonus:

#changement de liste
elif [ "$1" == "change" ]; then #condition requise : avoir au moins un argument qui soit "change"
	if [ $# == "2" ]; then #si il y a 2 arguments, alors
		TACHES="$2" #le 2eme argument est le chemin d'acces vers une nouvelle liste;
	else #s'il n'y en a qu'un, alors
		TACHES="$HOME/.todo_list" #on revient sur la liste de base
	fi
	echo "bascule sur la liste $TACHES"
#on a pas reellement d'erreurs possibles sur cette commande



#afficher la liste courante
elif [ $# == "1" ] && [ $1 == "current" ]; then
	echo "nous sommes dans la liste $TACHES" 


#help
elif [ $# == "1" ] && [ $1 == "help" ]; then
		echo "fonction ayant pour but de gerer une liste de tache de maniere simple;
plusieurs commandes sont a la disposition de l'utilisateur pour faciliter la gestion de cette liste :
-todo add N TASK : ajoute la tache TASK sur la ligne N de la liste courante (par defaut, $HOME/.todo_list). Si N est superieur au nombre de ligne, on l'ajoute en derniere position;

-todo done N : supprimme de la liste la ligne N. il est possible de renseigner plusieurs lignes a supprimer (si les lignes renseignees n'etant pas occupee, rien ne se passe);

-todo list : affiche la liste dans le terminal, avec le numero de ligne associee;

- todo change PATH: change le fichier ou est stocke la liste par la liste dont le chemin d'acces complet est "path"; si aucun chemin n'est transmis, on utilise la liste par defaut;

- todo current : affiche la liste courante;

todo help : affiche le texte ci-dessus
"

else
	echo "attention: commande invalide ('todo help' si vous ne savez pas par ou commencer)"
fi
else
	echo "attention: il faut fournir une commande a executer ('todo help' si vous ne savez pas par ou commencer)"
fi
}
