import socket as soc
import doctest

ex_requete_http1="GET /page1.html HTTP/1.1\r\nHost: localhost\r\nAccept-Language: fr-FR,en;q=0.3\r\nUser-Agent: Mozilla/5.0 Firefox/98.0\r\n\r\n"

ex_requete_http2="GET /pages/index.html HTTP/1.1\r\nHost: localhost\r\nAccept-Language: fr\r\n\r\n"
ex_requete_http3="GET /autres_pages/toto.html HTTP/1.1\r\nHost: localhost\r\n\r\n"

def decode_requete_http(requete) :
    """
    fonction prenant en entree une requete http et renvoyant un tuple compose de :
    - la chaine representant la page que l'on cherche a acceder;
    - un dictionnaire contenant les informations de la requete.

    >>> a,b = decode_requete_http(ex_requete_http1)
    >>> a == "/page1.html"
    True
    >>> len(b)
    3
    >>> b["Host"] == "localhost"
    True
    >>> b["Accept-Language"] == "fr-FR,en;q=0.3"
    True
    >>> b["User-Agent"] == "Mozilla/5.0 Firefox/98.0"
    True
    """
    pageLink = requete.split()[1] # on recupere le lien de la page
    splittedRequete = requete.split("\r\n")[1:-2:]  # on split la requete avec '\r\n' comme separateurs pour recuperer les parties qui nous interessent ensuite
    dico = {}                                       # les mots ainsi obtenus sont composes d'un intitule, de ':', et d'une valeur :
    for word in splittedRequete:
        key = word.split(":")[0]    # on recupere la cle, soit le mot avant les 2 points
        dico[key] = " ".join(word.split(" ")[1::]) # tout le reste est considere comme la valeur
    return pageLink,dico

def get_reponse(url_page) :
    """
    # fonction prenant en entree l'url d'une page et renvoyant la reponse http associe : une reponse avecun code 200 si elle est valide, 404 sinon
    >>> a = get_reponse("pages_serveur/fr/pages/index.html")
    >>> a == "HTTP/1.0 200 OK\\r\\nContent-Type:text/html\\r\\nContent-Length:73\\r\\n\\r\\n<!DOCTYPE html>\\n<html>\\n<body>\\n<h1>Voici index.html !</h1>\\n</body>\\n</html>\\r\\n"
    True
    >>> b = get_reponse("page_non_existante")
    >>> b == "HTTP/1.0 404 NotFound\\r\\nContent-Type:text/html\\r\\nContent-Length:172\\r\\n\\r\\n<!DOCTYPE html>\\n<html>\\n<head><title>404 Not Found</title></head><body>\\n<h1>Page non trouvée !!</h1>\\n<p>L'URL demandée n'a pas été trouvée sur ce serveur.</p></body>\\n</html>\\r\\n"
    True
    """
    try:
        file = open(url_page) # on recupere le fichier,
        fileContent = file.read() # sa taille ;
        code = "200 OK" # et on stocke 200.
    except FileNotFoundError: # si on a cette erreur, c'est que le fichier n'existe pas :
        file = open("pages_serveur/page404.html") # on fait donc comme aux lignes precedentes, mais avec la page 404
        fileContent = file.read()#.replace('\n','\r\n')
        code = "404 NotFound"
    size = len(fileContent) # on recupere ici la taille de notre fichier html

    return f"HTTP/1.0 {code}\r\nContent-Type:text/html\r\nContent-Length:{size}\r\n\r\n{fileContent}\r\n" # on renvoie toutes les infos

def traite_requete(requete) :
    """
    >>> traite_requete(ex_requete_http2) == get_reponse("pages_serveur/fr/pages/index.html")
    True
    >>> traite_requete(ex_requete_http3) == get_reponse("pages_serveur/en/autres_pages/toto.html")
    True
    """
    pageLink,dicoInfo = decode_requete_http(requete) # on recupere le lien de la page et le dico de la requete
    if "Accept-Language" in dicoInfo: # si on a une mention "Accept-Language"
        if dicoInfo["Accept-Language"][0:2] == 'fr': # on verifie qu'on demande du francais
            pageLink = f"pages_serveur/fr{pageLink}"  # dans ce cas, on met les pages en francais
        else:                                          # sinon on met de l'anglais
            pageLink = f"pages_serveur/en{pageLink}"
    else:
        pageLink = f"pages_serveur/en{pageLink}"
    return get_reponse(pageLink)

if __name__ == "__main__" :
    doctest.testmod(verbose=True)
    serveur = soc.socket(soc.AF_INET, soc.SOCK_STREAM)
    serveur.bind(("127.0.0.1", 8080))
    while True:
        serveur.listen()
        socket_client, addr = serveur.accept() # socket client et son adresse
        print(addr)
        data = socket_client.recv(65535) # données transmises
        print(data.decode())
        
        socket_client.send(traite_requete(data.decode()).encode())
