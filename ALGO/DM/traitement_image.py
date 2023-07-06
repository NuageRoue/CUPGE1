import matplotlib.pyplot as plt
import matplotlib.image as img
import numpy as np

# traitements préliminaires
def neg(im) :
    return 1 - im # on renvoie 1 - im, soit le negatif de la matrice

def miroir(im) :
    return im[:,::-1] # on renvoie la matrice en inversant le contenu des lignes (donc on renvoie la matrice inverse horizontalement)

def plus_de_lumiere(im,d) :
    return np.clip(im + d, 0, 1) # avec np.clip, on plafonne les valeurs de notre matrice + d entre 0 et 1 

def plus_de_contraste(im,k) :
    return np.clip(im + k * (im - 0.5), 0, 1) # meme chose ici, on plafonne les valeurs de notre matrice (a laquelle on applique notre fonction augmentant le contraste) entre 0 et 1


# photomaton
def photomaton(im) :        
    imA = im[0::2,0::2] # lignes paires, colonnes paires : image du coin haut gauche
    imB = im[0::2,1::2] # lignes paires colonnes impaires : image du coin haut droit
    imC = im[1::2,0::2] # lignes impaires, colonnes paires : image du coin bas gauche
    imD = im[1::2,1::2] # lignes impaires, colonnes impaires : image du coin bas droit 
    
    imageHaut = np.concatenate((imA,imB), axis=1) # on va concatener les 2 images du haut (soit le "cote")
    imageBas = np.concatenate((imC,imD), axis=1) # on va concatener les 2 images du bas selon l'axe 1 (soit le "cote")
    return np.concatenate((imageHaut,imageBas), axis=0) # on va concatener les 2 images generee precedemment, selon l'axe 0 (soit le "dessous")

def mlgk(im, k):
    if k > 0 : 
        return mlgk(photomaton(im), k-1) # on renvoie la fonction appliquee au photomaton de l'image en entree (permettant donc d'appliquer photomaton plusieurs fois)
    return im # cas d'arret, on renvoie l'image une fois k = 0


#réduction du poids d'une image
# Réduction du nombre de couleurs
def f(x, b) :
    deux_b = 2**b
    return int(deux_b * int(255*x)/256)/(deux_b-1)

def moins_de_coul(im, b) :
    func = np.vectorize(f) # la fonction vectorize de numpy adapte une fonction a une matrice, permettant de prendre en entree une matrice et de renvoyer... une matrice, mais a laquelle on applique la fonction d'origine a tous les elements
    return func(im,b)

def moins_de_pix(im, k) :
    return im[::k,::k] # on effectue un slicing en prenant un pixel sur k sur chaque ligne et chaque colonne

def moins_de_pix2(im, k) :
    shape = (im.shape[0]//k, im.shape[1]//k) # on prend la taille de l'image d'origine, divisee par k
    new_im = np.zeros(shape) # on prepare une nouvelle image faisant cette taille
    for i in range(new_im.shape[0]):
        for j in range(new_im.shape[0]):
            new_im[i,j] = np.mean(im[i * k:(i + 1) * k:,j * k:(j + 1) * k:])  # pour chaque pixel (i,j) de cette nouvelle matrice, on lui attribue la valeur de la moyenne de la matrice [i * k:(i + 1) * k:,j * k:(j + 1) * k:]
                                                                                # (soit une petite portion de la matrice d'origine, de taille k*k)
    return new_im


#réduction du bruit : filtre médian
def filtre_median(im, q) :
    new_im = np.zeros(im.shape) # on genere une matrice vide de la meme taille que notre image
    for i in range(im.shape[0]):
        for j in range(im.shape[1]):
            new_im[i,j] = np.median(im[max(0,i - q):min(i + q + 1,im.shape[0]),max(0,j - q):min(j + q + 1,im.shape[0])])    # chaque pixel (i,j) de la nouvelle matrice correspond au median du pixel (i,j) de l'image d'origine et de ses pixels voisins
                                                                                                                            # (on prends les voisins en utilisant le maximum entre 0 et i - q pour eviter de "sortir de l'image" (meme si en python cela revient plus a aller a la fin de l'image avec les valeurs negatives)
                                                                                                                            # idem avec le minimum entre la taille de l'image et i + 1 + q)
    return new_im


#arbre quaternaire et compression
def init(k):
    return np.zeros((2**k,2**k)) # on genere une liste de taille 2**k par 2**k

def arbre_to_image(qt,i,j,k,im):
    if type(qt) == list: # si on a en entree une liste, dans ce cas on doit diviser notre matrice im en 4 parties de part egale
        k -= 1 #etant donne que la largeur/hauteur de l'image est de 2**k, alors 2**k-1 est la moitie de 2**k
        arbre_to_image(qt[0],i,j,k,im) # partie en haut a gauche : le coin haut reste le meme
        arbre_to_image(qt[1],i,j+2**k,k,im) # partie en haut a droite : le coin haut est (i, j+2**k ou k a ete decremente, on ajoute donc a j la moitie de la largeur initiale)
        arbre_to_image(qt[2],i+2**k,j,k,im) # partie en bas a gauche : le coin haut est (i+2**k,j ou k a ete decremente, on ajoute donc a i la moitie de la largeur initiale)
        arbre_to_image(qt[3],i+2**k,j+2**k,k,im) # partie en bas a droite : le coin haut est (i+2**k,j+2**k ou k a ete decremente, on ajoute donc a i et j la moitie de la largeur initiale)
    else: # on verifie d'abord que qt est une liste plutot qu'un entier, car cela posait probleme avec image_to_arbre
        im[i:i+2**k,j:j+2**k] = qt #sinon, qt est un entier : dans ce cas, toute la zone etudiee (im[i:i+2**k,j:j+2**k]) vaut qt

def new_coul(x,nbc) :
    return int(x * (nbc - 1)) # on renvoie notre valeur x transposee en nuance de gris

def test(im, i, j, k, nbc) :
    if new_coul(im[i:i+2**k,j:j+2**k].min(),nbc) == new_coul(im[i:i+2**k,j:j+2**k].max(),nbc): #pour avoir une fonction rapide, on ne verifie que si le plus grand element et le plus petit de notre matrice ont bien la meme nuance de gris
        return True, new_coul(im[i:i+2**k,j:j+2**k].min(),nbc)
    return False, -1

def image_to_arbre(im, i, j, k, nbc) :

    t = test(im,i,j,k,nbc)
    if t[0]: # si la zone etudiee est bien d'une seule nuance de gris,
        return t[1] # on renvoie simplement la valeur de cette nuance de gris
    k -= 1 # sinon, on divise la zone en 4 (comme explique sur la fonction arbre_to_image)
    elemA = image_to_arbre(im, i, j, k, nbc) # on applique la fonction sur les 4 zones, en modifiant i,j et k 
    elemB = image_to_arbre(im, i, j+2**k, k, nbc)
    elemC = image_to_arbre(im, i+2**k, j, k, nbc)  
    elemD = image_to_arbre(im, i+2**k, j+2**k, k, nbc)
    return [elemA,elemB,elemC,elemD] # on renvoie la liste des 4 valeurs (eux memes des entiers ou des listes a 4 valeurs)

def taille(qt) :
    if type(qt) == list:
        return taille(qt[0]) + taille(qt[1]) + taille(qt[2]) + taille(qt[3])
    return 1

if __name__ == "__main__" :

    # récupération des images
    june = img.imread('june.png')
    june = (june[:,:,0]+june[:,:,1]+june[:,:,2])/3
    juneBruit = img.imread('juneBruit.png')
    juneBruit = (juneBruit[:,:,0]+juneBruit[:,:,1]+juneBruit[:,:,2])/3
    paresseux = img.imread('paresseux.png')
    paresseux = (paresseux[:,:,0]+paresseux[:,:,1]+paresseux[:,:,2])/3
    
    plt.imshow(june,plt.cm.gray,)
    plt.title("june")
    plt.show()

    negJune = neg(june)
    plt.imshow(negJune,plt.cm.gray)
    plt.title("neg(june)")
    plt.show()

    mirrorJune = miroir(june)
    plt.imshow(mirrorJune,plt.cm.gray)
    plt.title("miroir(june)")
    plt.show()
    
    lightJune = plus_de_lumiere(june, .4)
    plt.imshow(lightJune,plt.cm.gray)
    plt.title("plus_de_lumiere(june, .4)")
    plt.show()
    
    contJune = plus_de_contraste(june,2)
    plt.imshow(contJune,plt.cm.gray)
    plt.title("plus_de_contraste(june,2)")
    plt.show()
    
    photomatonJune = photomaton(june)
    plt.imshow(photomatonJune,plt.cm.gray)
    plt.title("photomaton(june)")
    plt.show()
    
    mlJune = mlgk(june,8)
    plt.imshow(mlJune,plt.cm.gray)
    plt.title("mlgk(june,8)")
    plt.show()
    
    lessJune = moins_de_coul(june,2)
    plt.imshow(lessJune,plt.cm.gray)
    plt.title("mois_de_coul(june,2)")
    plt.show()
    
    lessPix = moins_de_pix(june,8)
    plt.imshow(lessPix,plt.cm.gray)
    plt.title("moins_de_pix(june,8)")
    plt.show()
    
    lessPix2 = moins_de_pix2(june,8)
    plt.imshow(lessPix2,plt.cm.gray)
    plt.title("moins_de_pix_2(june,8)")
    plt.show()
    
    plt.imshow(juneBruit,plt.cm.gray)
    plt.title("juneBruit")
    plt.show()

    filtre = filtre_median(juneBruit,4)
    plt.imshow(filtre,plt.cm.gray)
    plt.title("filtre_median(juneBruit,4)")
    plt.show()
    
    
    qt0 = [[2, 0, 0, 2], 1, [2, 1, 2, 1], 0]
    im0 = init(10)
    arbre_to_image(qt0,0,0,10,im0)
    plt.imshow(im0,plt.cm.gray)
    plt.title("im0 (arbre_to_image(qt0,0,0,10,im0))")
    plt.show()
    
    plt.imshow(paresseux,plt.cm.gray)
    plt.title("paresseux")
    plt.show()

    qt1 = image_to_arbre(paresseux,0,0,10,5)
    im1 = init(10)
    arbre_to_image(qt1,0,0,10,im1)
    plt.imshow(im1,plt.cm.gray)
    plt.title("im1 (image_to_arbre(paresseux,0,0,10,5))")
    plt.show()
    
    print(f"qt0 contient {taille(qt0)} elements")
    print(f"qt1 contient {taille(qt1)} elements, contre {1024 * 1024} pixels pour une image classique en 1024 par 1024")
