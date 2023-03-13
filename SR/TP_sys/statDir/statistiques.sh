#!/bin/bash


# objectif :
# On veut obtenir des statistiques sur des dossiers/fichiers contenusdans le dossier courant, telles que :
#	- la taille totale occupée
#	- la taille occupée par les fichiers, les répertoires cachées
#	- le nombre de petits et gros fichiers (- de 512Ko // + de 15Mo)
#	- les fichiers et répertoires vides pouvant être supprimés
#	- des statistiques sur les extensions, types de fichiers (scripts python, fichier html, executable...)

# 3 modes de fonctionnement peuvent être effectués :
#	- mode 1 ("1" ou rien en argument) : peu de détails (seulement la taille globale, le nombre de fichiers/dossiers)

#	- mode 2 ("2" en argument) : un peu plus de détails (nombre de fichiers/répertoires cachés, fichiers/répertoires cachés);

#	- mode 3 ("3" ou plus en argument): toutes les infos (les gros et petits fichiers, le plus gros fichiers, le listing des types de fichiers (avec des pourcentages ?)

function out() {
	# fonction affichant a proprement parler les differentes infos. elle prend en entree un nombre entre 1 et 3 definissant les details apportees a la reponse
	# chaque information est affichee dans un test, qui determine si telle ou telle info doit etre affichee au pluriel ou non
	echo "Analyse de $(pwd) :"
	# quoi qu'il arrive on affiche le nombre de dossiers :
	if [ $NB_DIR -gt "1" ];then
		echo "  - $NB_DIR répertoires" 
	else
		echo "  - $NB_DIR répertoire" 		
	fi

	if [ "$1" -gt 1 ]; then #si on demande un niveau de detail superieur a 1, on affiche :
		if [ $NB_DIR -ge "1" ];then # on affiche le nombre de dossiers caches/vides si on a au moins un dossier	
			#affichage des dossiers caches
			if [ $NB_HIDDEN_DIR -gt "1" ];then
				echo "      - $NB_HIDDEN_DIR répertoires cachés"
			else
				echo "      - $NB_HIDDEN_DIR répertoire caché"
			fi

			#affichage des dossiers vides
			if [ $NB_EMPTY_DIR -gt "1" ];then
				echo "      - $NB_EMPTY_DIR répertoires vides" #dossiers vides
			else
				echo "      - $NB_EMPTY_DIR répertoires vide" #dossier vide	
			fi
		fi

		#affichage des fichiers :
		if [ $NB_FILE -gt "1" ];then
			echo "  - $NB_FILE fichiers dont" #total de fichier
		elif [ $NB_FILE -ge "1" ];then
			echo "  - $NB_FILE fichier soit"	
		else
			echo "  - $NB_FILE fichier"
		fi

		# on affiche les differentes caracteristiques des fichiers si on a au moins un fichier
		if [ $NB_FILE -ge "1" ];then

			#affichage des fichiers caches :
			if [ $NB_HIDDEN_FILE -gt "1" ];then
				echo "      - $NB_HIDDEN_FILE fichiers cachés" #fichiers caches
			else
				echo "      - $NB_HIDDEN_FILE fichier caché" #fichiers caches	
			fi

			#affichage des fichiers vides :
			if [ $NB_EMPTY_FILE -gt "1" ];then
				echo "      - $NB_EMPTY_FILE fichiers vides" #fichiers vides
			else
				echo "      - $NB_EMPTY_FILE fichier vide" #fichiers vides
			fi
			
			if [ "$1" -gt "2" ]; then #si le niveau de details demande est superieur a 2, alors on affiche aussi
		
				# affichage des petits fichiers :
				if [ $NB_SMALL_FILE -gt "1" ];then
					echo "      - $NB_SMALL_FILE fichiers de moins de 512Ko" #le nombre de petit fichier
				else
					echo "      - $NB_SMALL_FILE fichier de moins de 512Ko" #le nombre de petit fichier
				fi

				# affichage des gros fichiers :
				if [ $NB_BIG_FILE -gt "1" ];then
					echo "      - $NB_BIG_FILE fichiers de plus de 15Mo" # le nombre de gros fichier
				else
					echo "      - $NB_BIG_FILE fichier de plus de 15Mo" # le nombre de gros fichier
				fi

				# affichage du plus gros fichier :
				echo "      - le plus gros fichier est $BIGGEST_FILE" # le plus gros fichier	

				#affichage des types de fichiers
				echo "    Il y a :" # les types de fichiers
				
				if [ "$NB_PY" -gt "1" ];then
					echo "      - $NB_PY fichiers python"
				else
					echo "      - $NB_PY fichier python"
				fi

				if [ "$NB_IMG" -gt "1" ];then
					echo "      - $NB_IMG fichiers image"
				else
					echo "      - $NB_IMG fichier image"
				fi

				if [ "$NB_VID" -gt "1" ];then
					echo "      - $NB_VID fichiers vidéo"
				else
					echo "      - $NB_VID fichier vidéo"
				fi

				# ici, la commande que j'utilisais pour les types de fichiers avant de savoir ce qui etait reellement attendu.
				# find -type f | xargs -I {} file -b {} | awk -F, '{print $1}' | sort | uniq -c | sed 's/^/      - /'
				#detail de comment le resultat est obtenu : 
				# - on recupere avec find tous les fichiers;
				# - grace a xargs on utilise find sur chaque fichier ainsi obtenu, -b assurant de ne pas afficher le nom du fichier
				# - avec awk en precisant que notre separateur est une virgule (,), on n'affiche que le premier "mot" de chaque ligne, correspondant au type de fichier
				# - on trie cette liste de type de fichier par ordre alphabetique avec sort
				# - uniq -c permet de lister chaque occurence de type, de n'en afficher qu'une precedee du nombre reel d'occurence (on liste par type)
				# - sed permet de modifier chaque ligne en y ajoutant un tiret et des espaces.
			fi
		fi
	else # si on a un niveau de detail minime
		if [ $NB_FILE -gt "1" ];then
		echo "  - $NB_FILE fichiers" # on affiche seulement le nombre de fichiers
		else
		echo "  - $NB_FILE fichier"
		fi
	fi
	echo "  - taille totale : $ESPACE_OCCUPE" # dans tous les cas on affiche l'espace disque occupe
}

function statistiques () {
	# les donnees importantes sont generes si elles sont utiles, evitant ainsi un temps de calcul inutile
	NB_DIR=$[$( find -type d | wc -l ) - 1] #tous les dossiers, c'est a dire le resultat de la commande ci-contre moins 1 (le repertoire courant, non compris dans son propre contenu)
	NB_FILE=$(find -type f | wc -l ) #idem, les fichiers contenus, soit le resultat de la commande ci-contre
	ESPACE_OCCUPE=$(du -h | tail -n 1 |awk '{ print $1 }') #du -h permet d'afficher l'espace occupe, en unite raisonnable. avec tail et awk, on affiche seulement le total
	if [ "$#" -eq "1" ] && [[ "$1" =~ ^[0-9]+$ ]];then # on s'assure de n'avoir pas plus d'un argument en entree, qui soit forcement un nombre
		if [ "$#" -eq "0" ] || [ "$1" -le "1" ];then # si on ne fournit pas d'argument, ou qu'on fournit 0 ou 1 on passe en mode peu de détails
			out 1
		elif [ $1 -eq "2" ];then # si on fournit 2, on passe en mode plus de détails
			NB_HIDDEN_DIR=$[ $(find -type d -printf "%f\n" | grep -c ^[\.]) - 1 ] # pour les dossiers caches, on prend seulement le nom du dossier en compte (ce que fait -printf "%f\n", ce qui qffiche tous les noms separes par un saut de ligne). ensuite, avec grep, on compte tous ceux commencant par un point, moins 1
			NB_HIDDEN_FILE=$(find -type f -printf "%f\n" | grep -c ^[\.]) #idem, mais sans le moins 1 (et sur les fichiers)
			NB_EMPTY_DIR=$( find -type d -empty | wc -l ) # l'argument empty permet de recuperer les dossiers (et/ou fichiers) vides. en associant cette commande avec wc -l, on obtient le nombre de dossier/fichiers vides
			NB_EMPTY_FILE=$( find -type f -empty | wc -l )

			out 2
		else # sinon (3 ou plus), on passe en mode tous les détails
			NB_HIDDEN_DIR=$[ $(find -type d -printf "%f\n" | grep -c ^[\.]) - 1 ] # pour les dossiers caches, on prend seulement le nom du dossier en compte (ce que fait -printf "%f\n", ce qui qffiche tous les noms separes par un saut de ligne). ensuite, avec grep, on compte tous ceux commencant par un point, moins 1
			NB_HIDDEN_FILE=$(find -type f -printf "%f\n" | grep -c ^[\.]) #idem, mais sans le moins 1 (et sur les fichiers)
			NB_EMPTY_DIR=$( find -type d -empty | wc -l ) # l'argument empty permet de recuperer les dossiers (et/ou fichiers) vides. en associant cette commande avec wc -l, on obtient le nombre de dossier/fichiers vides
			NB_EMPTY_FILE=$( find -type f -empty | wc -l )
			NB_BIG_FILE=$(find -type f -size +15M | wc -l) #avec size, on peut recuperer tel ou tel fichier d'une taille superieur ou inferieur a celle mentionnee.
			NB_SMALL_FILE=$(find -type f -size -512k | wc -l)
			BIGGEST_FILE=$(find -type f -printf "%s $(pwd)/%P\n" | sort -n | tail -1 | awk '{print $2}') # avec -printf, on peut choisir le format renvoye par find. on precise, avec %s, que l'on souhaite affiche la taille du fichier puis son nom. ensuite, on trie avec sort, puis on affiche le dernier element (soit le plus gros) avec tail et awk (qui permet d'afficher le nom et pas la taille).
			NB_PY=$(find -type f -name "*.py" | wc -l)
			NB_IMG=$(find -type f -name "*.jpg" -o -name "*.png" | wc -l)
			NB_VID=$(find -type f -name "*.avi" -o -name "*.mp4" | wc -l)

			out 3
		fi
	elif [ "$#" -lt "1" ];then
		out 1
	else
		echo "attention: il faut fournir en entrée un chiffre compris entre 1 et 3 correspondant au niveau de détail demandé."
	fi
}



