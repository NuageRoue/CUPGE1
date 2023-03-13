#!/bin/bash

##objectif : on fournit en entree du programme 2 choses : une liste au format csv et une adresse de dossier. la liste contient sur chaque ligne:
#nom;prenom;date de naissance;mail

#a partir de cette liste, on veut creer une arborescence de dossier avec: 
#pour chaque ligne, un dossier dont nom est compose des 2 premieres lettres du prenom suivi des 7 premieres lettres du nom (sans espaces)
#ce dossier doit contenir 2 dossiers (Documents et Images) et un fichier mot_de_passe.txt, contenant un mot de passe.

#format du mot de passe:
#consonne-voyelle-consonne-voyelle-chiffre-chiffre-chiffre-chiffre



#Clement Oliveira
#generation du mot de passe:
function MDP_GEN () {
	#fonction qui genere un mot de passe a partir du fichie /dev/urandom et le stocke dans un fichier;

	#la recuperation d'un caractere est l'association de :
	#une ou plusieurs commande tr -d ou -dc qui ne recupere qu'un certain type de caracteres (des chiffres, des consonnes, des voyelles...);
	#une commande fold -w 1 qui organise le resultat en lignes d'un caractere de long;
	#une commande head -n 1 qui ne garde que la premiere ligne, et donc un seul caractere.
		
	MOTDEPASSE=$( cat /dev/urandom | tr -dc 'a-z' | tr -d 'aeiouy' | fold -w 1 | head -n 1 ) #on ajoute une consonne
	MOTDEPASSE+=$( cat /dev/urandom | tr -dc 'aeiouy' |fold -w 1 | head -n 1 ) #on ajoute une voyelle
	MOTDEPASSE+=$( cat /dev/urandom | tr -dc 'a-z' | tr -d 'aeiouy' | fold -w 1 | head -n 1 ) #on ajoute une consonne
	MOTDEPASSE+=$( cat /dev/urandom | tr -dc 'aeiouy' |fold -w 1 | head -n 1 ) #on ajoute une voyelle
	MOTDEPASSE+=$( cat /dev/urandom |  tr -dc '0-9' |fold -w 1 | head -n 1 ) #on ajoute un chiffre
	MOTDEPASSE+=$( cat /dev/urandom |  tr -dc '0-9' |fold -w 1 | head -n 1 ) #on ajoute un chiffre
	MOTDEPASSE+=$( cat /dev/urandom |  tr -dc '0-9' |fold -w 1 | head -n 1 ) #on ajoute un chiffre
	MOTDEPASSE+=$( cat /dev/urandom |  tr -dc '0-9' |fold -w 1 | head -n 1 ) #on ajoute un chiffre
}

function FILE_CHECK () {
	#fonction qui verifie si le fichier fourni en argument est bien un fichier .csv compose de lignes de 4 elements separes par des ";"
	if [[ $FILE == *.csv ]]; then #si le fichier est bien termine par .csv
		cat "$FILE" | while read LINE ; do #on lit toutes les lignes une par une
			if ! [ $( echo "$LINE" | awk -F";" '{ print NF }' ) -eq "4" ]; then #si la ligne lue ne contient pas 4 elements, alors
				echo "attention: le fichier fourni en entree n'a pas la bonne mise en forme. la generation des dossiers n'a pas pu aboutir"
				return 1; #on renvoie 1, ce qui stoppe la generation (cf ligne 53)
			else
			#on verifie que les noms et prenoms sont bien composes d'au moins une lettre
				if ! [ $( echo "$LINE" | awk -F";" '{ print $1 }' | tr -dc "a-z" | wc -m ) -gt "0" ];then #on retire tous les caracteres sauf les lettres avec tr -dc, puis on compte les caracteres restants avec wc -m
					echo "attention: le nom doit etre compose de lettres pour etre utilisable. La generation des dossiers n'a pas pu aboutir"
					return 1
				fi
				if ! [ $( echo "$LINE" | awk -F";" '{ print $2 }' | tr -dc "a-z" | wc -m ) -gt "0" ];then
					echo "attention: le prenom doit etre compose de lettres pour etre utilisable. La generaion des dossiers n'a pas pu aboutir"
					return 1
				fi
			fi
		done
	else #si le fichier n'est meme pas fini par csv, alors
		echo "attention, le fichier n'est pas un fichier csv. la generation des dossiers n'a pas pu aboutir";
		return 1; #meme scenario que ligne 38 
	fi
}

#lecture du fichier csv, reel point d'entree du programme.
if [ "$#" -eq "2" ]; then #il faut bien avoir 2 arguments;
	if [ -f "$1" ] && [ -d "$2" ]; then #on verifie que le fichier et le dossier specifies existent
		FILE="$1"
		FILE_CHECK
		RESULT=$? #on stocke dans la variable RESULT la valeur de retour de la fonction FILE_CHECK
		if [ "$RESULT" -eq "0" ]; then #si ce resultat vaut 1, le fichier est valide. donc on peut generer le dossier utilisateur
			cat "$1" | while read LINE ; do #pour chaque ligne (chaque utilisateur donc)
				ID=$( echo "$LINE" | awk -F";" '{print $2}' |tr -dc "a-z" | cut -c1-2 | tr -d '\n' ) #on recupere les 2 premieres LETTRES du prenom de l'utilisateur pour generer un dossier
				ID+=$( echo "$LINE" | awk -F";" '{print $1}' | tr -dc "a-z" | cut -c1-7 ) #et les 7 premieres de son nom
				if [ -d "$2/$ID" ]; then #si un dossier porte deja ce nom, on ne peut pas le regenerer :
					SUFFIXE="1"
					while [ -d "$2/$ID$SUFFIXE" ]; do #on doit ajouter un suffixe numerique qu'on incremente jusqu'a ce qu'aucun dossier ne porte ce nom
						SUFFIXE=$[ $SUFFIXE + 1 ]
					done
					ID=$ID$SUFFIXE
				fi
				echo "generation du dossier $ID" 
				mkdir "$2/$ID" #on genere le dossier et son contenu
				mkdir "$2/$ID/Documents" 
				mkdir "$2/$ID/Images"
				echo "mot de passe : " | tr -d "\n" > "$2/$ID/mot_de_passe.txt"
				MDP_GEN #on genere un mot de passe unique
				echo "$MOTDEPASSE" >> "$2/$ID/mot_de_passe.txt"
			done
		fi
	
	else
		if ! [ -f "$1" ]; then #on ne fait rien si les arguments sont invalides. on se contente de prevenir l'utilisateur
			echo "attention: le premier argument doit etre un fichier csv existant. la generation n'a pas pu aboutir."
		fi
		if ! [ -d "$2" ]; then
			echo "attention: le deuxieme argument doit etre un dossier existant. l'operation n'a pas pu aboutir."
		fi
	fi
else
	echo "attention: pour generer un espace de travail, il faut fournir une liste d'etudiant et un dossier ou le creer"
fi
