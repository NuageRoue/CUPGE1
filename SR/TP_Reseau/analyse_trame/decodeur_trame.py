import struct
import doctest
import socket

ex_udp = b'\x00-\xd9\x9e\x00\x0eR\x8ccoucou'
ex_tcp = b'\x00-\xd7[\x00\x00\x17\x15\x00\x00\x04e\x86\xc6\ndg!By!\xaf\xff&\xfc\x19R\xcc\x18\xac|(coincoin'
ex_icmp = b'\x05\x04g\x90\x1a@\xc9\x01'
ex_ip = b"H\xf7\x00&[\x0cI\r\xe5\x01v5\xea\xd8\xa0\xe5L\xda\x86\x93\x0e\xa0\xed\xe8\x99\xc1G\xc0{P'\xc4cuicui"
ex_eth = b'R\x0c\xc7\x1d\xca578\x1fUk\x98\x08\x00coicoi'

ex_complet1 = b'Q\xf0\xdeG?\xf4\xa0\x18\x12f\xde\xd5\x08\x00H$\x00(\x85\xc2\x11\xcc\x83\x01\xf1\x94\xff\xfc\xbf\x067\x17\xd9\x86\xd4\x96\xbf\xdfdv$a\xae\x01\xd0\x90\n\x07\x1d\xfd\xdb\t3\xad'
ex_complet2 = b'\xb3\x82\x90ze\xe66?HJ#9\x08\x00Hu\x00G\\S\n{\r\x06\x0f\x93\x1f\xc9\xa5\xd0\xac\xea\xbc\xea\xc4\x13a\xdet>\xe1\x13\x9cJ\x8f\x1b\x03\x15\xf5\x83\x00\x00\x11L\x00\x00\r\xea\x80:\\\x9dJ\x9c)\xaf\xba\xcc){\xc0\x97\x83\xc4\xcd\xec3\xb4bravo !'
ex_complet3 = b"\x8e`\x1cV\xbf\x86\xa6\x0b\x8f\x99\xe8\x1e\x08\x00H>\x001\x1e*\xd4\xc5\x13\x11\xb20W'\xce*\xdb+\xc4\xa7\x08}\x99\xfd\xd9\x90\x9d\x1cA/\x1f\x00\x02\x99\xddG\x00\x11\xda\x9asuper ;-)"

def decode_udp(data) :
    """

    fonction prenant en parametre un tableau d'octets représentant un datagramme UDPet retournant un couple composé de :
    - une chaine représentant les informations de l'en-tête UDP
    - les données contenues dans le segment UDP (ce qui suit l'en-tête donc)

    info datagramme UDP :
    - la taille de l'entête est fixe, et mesure 8 octets :  
        - les 2 premiers octets représentent le port source
        - les 2 octets suivant représentent le port de destination
        - les 2 octets suivants représentent la longueur
        - les 2 octets suivants représentent la somme de contrôle
    - les octets suivants représentent les données échangées

    >>> a = decode_udp(ex_udp)
    >>> len(a) == 2
    True
    >>> a[0] == "        +++ Paquet UDP +++\\n            Port source      : 45\\n            Port destination : 55710\\n            Longueur totale  : 14\\n"
    True
    >>> a[1].decode('utf-8') == "coucou"
    True
    """
    
    
    
    enTete = struct.unpack("!HHHH", data[0:8]) # on va decoder seulement l'enTete : on recupere un tuple contenant port source, port de destination, longueur et somme de controle ;
    
    donneeTransmises = data[8:len(data)] # les donnees transmises correspondent à tout le reste, on ne les decode pas


    return f"        +++ Paquet UDP +++\n            Port source      : {enTete[0]}\n            Port destination : {enTete[1]}\n            Longueur totale  : {enTete[2]}\n",donneeTransmises # on renvoie bien la chaine de caractère contenant les infos et les données transmises non décodées


def decode_tcp(data) :
    """
    le datagramme TCP est composé d'un entête d'une taille minimale de 20 octets :
    - sur 2 octets, on a le port source [0:2]
    - sur 2 octets, le port destination [2:4]
    - sur 4 octets, le numéro de séquence [4:8]
    - sur 4 octets, le numéro de séquence acquitté [8:12]
    - sur 2 octets, on a : [12:14]
        - LET, la longueur de l'en-tête sur 4 bits (exprimée en mots de 4 octets)
        - 6 bits réservé
        - les FLAGS sur 6 bits
    - sur 2 octets on a la taille de fenêtre [14:16]
    - sur 2 octets, la somme de contrôle [16:18]
    - sur 2 octets, le pointeur d'urgence [18:20]
    - ensuite, sur LET (en octets) - 20 octets, les options/bourrage
    enfin, sur len(data) - LET (en octets) octets, les données utiles (les données transmises donc) 
    

    >>> a = decode_tcp(ex_tcp)
    >>> len(a) == 2
    True
    >>> a[0] == "        +++ Paquet TCP +++\\n            Port source      : 45\\n            Port destination : 55131\\n            Longueur en-tête : 8\\n"
    True
    >>> a[1].decode('utf-8') == "coincoin"
    True
    """
    
    enTete = struct.unpack("!HHLLHHHH", data[0:20]) # on decode la partie fixe de l'entete, qui plus est la seule partie relativement utile pour le programme
    LET = (enTete[4] >> 12) # la longueur de l'entête, exprimée en mots de 4 octets

    donneeTransmises = data[LET * 4:len(data)] # on récupère les données transmises, sans les décoder : on utilise LET exprimée en octets pour savoir quand effectuer un slicing
    
    # on renvoie une formatted string dans laquelle on indique les informations qui nous sont utiles : le port source, le port destination et la longueur de l'en-tête
    return f"        +++ Paquet TCP +++\n            Port source      : {enTete[0]}\n            Port destination : {enTete[1]}\n            Longueur en-tête : {LET}\n",donneeTransmises



def decode_icmp(data) :
    """
    fonction prenant en entrée un datagramme icmp encodé, retournant une chaine de caractère détaillant quelques informations sur ce datagramme.
    
    format du datagramme icmp :
        - un octet correspondant au type
        - un octet correspondant au code
        - 2 octets correspondant à la somme de contrôle
        - 4 octets non-utilisés
        - les données optionnelles

    >>> a = decode_icmp(ex_icmp)
    >>> a == "        +++ Paquet ICMP +++\\n            Type             : 5\\n"
    True
    """


    enTete = struct.unpack("!BBHL",data) # on décode seulement l'entête, la seule chose qui nous soit utile (et dont on est sûr qu'elle existe)
                                         # on se retrouve donc avec un tuple composé du type, du code, de la somme de contrôle et de la "partie inutilisée"

    # on renvoie ici aussi une formatted string contenant les informations demandées (le type de donnée)
    return f"        +++ Paquet ICMP +++\n            Type             : {enTete[0]}\n"

def decode_adresse_IP(addr) :
    """
    >>> decode_adresse_IP(2475088460) == "147.134.218.76"
    True
    """
    addrUnpacked = (addr >> 24, (addr >> 16) % 2**8, (addr >> 8) % 2**8, addr % 2**8) # on récupère un tuple contenant les 4 valeurs des 4 octets

    return f"{addrUnpacked[0]}.{addrUnpacked[1]}.{addrUnpacked[2]}.{addrUnpacked[3]}" # on renvoie une formatted string contenant ces 4 valeurs

def decode_ip(data) :
    """

    fonction prenant en entrée un datagramme ip et renvoyant un triplet composé d'une chaine de caractère contenant les informations du paquet ip, le numéro associé au protocole associé (1 pour ICMP, 6 pour TCP, 17 pour UDP...) et enfin, les données encapsulées.
    
    >>> a = decode_ip(ex_ip)
    >>> len(a) == 3
    True
    >>> a[0] == '    --- Paquet IP ---\\n        Version          : 4\\n        Longueur en-tête : 8\\n        Protocole        : 1\\n        Adresse source   : 234.216.160.229\\n        Adresse dest.    : 76.218.134.147\\n'
    True
    >>> a[1] == 1
    True
    >>> a[2].decode('utf-8') == "cuicui"
    True
    """
    
    enTete = struct.unpack("!HHHHHHLL", data[0:20]) # on décode la partie fixe de l'en-tête

    version = (enTete[0] >> 12) # les 4 premiers bits de l'en-tête correspondent à la version
    LET = ((enTete[0] >> 8) % 2**4) # les 4 suivants correspondent à la longueur de l'entête : on récupère le premier octet et on enlève les 4 premiers bits de cet octets
    protocol_id = enTete[4] % 2**8 # l'identifiant du protocole correspond aux 4 derniers bits du 5eme mot de 2 bits
    addrSource = decode_adresse_IP(enTete[6]) # l'adresse source
    addrDest = decode_adresse_IP(enTete[7]) #l'adresse de destination 
    donnees = data[LET * 4:len(data)] # les données transmises (potentiellement un protocole encapsulé donc), allant de LET * 4 (soit LET exprimée en octet) jusqu'à la fin

    return f'    --- Paquet IP ---\n        Version          : {version}\n        Longueur en-tête : {LET}\n        Protocole        : {protocol_id}\n        Adresse source   : {addrSource}\n        Adresse dest.    : {addrDest}\n',protocol_id,donnees # on renvoie le triplet demandé


def decode_mac(data) :
    """
    fonction prenant en entrée une chaine d'octets renvoyant l'adresse mac décodée

    >>> decode_mac(b'R\\x0c\\xc7\\x1d\\xca5') == "52:0c:c7:1d:ca:35"
    True
    """

    addrUnpacked = struct.unpack("!BBBBBB", data) # on décode les 6 octets dans un tuple
    '''
    straddr = ""    
    for elem in addrUnpacked:
        stradd += hex(elem)[2:len(hex(elem))] if len(hex(elem)) > 3 else "0"+hex(elem)[2:len(hex(elem))]
        stradd+=":"
    '''

    
    return f"{'%.2x' % addrUnpacked[0]}:{'%.2x' % addrUnpacked[1]}:{'%.2x' % addrUnpacked[2]}:{'%.2x' % addrUnpacked[3]}:{'%.2x' % addrUnpacked[4]}:{'%.2x' % addrUnpacked[5]}" # l'expression '%.2x' % n permettant d'obtenir une représentation en hexadécimal de n


def decode_Ethernet(data) :
    """
    fonction prenant en entrée une chaine de bits représenant une trame Ethernet, (sans FCS) renvoyant un triplet composé de : 
    - une chaine de caractère recensant les informations de l'en-tête
    - le numéro du protocole encapsulé
    - les données encapsulées (potentiellement un protocole encapsulé donc)
    >>> a = decode_Ethernet(ex_eth)
    >>> len(a) == 3
    True
    >>> a[0] == '>>> Trame Ethernet <<<\\n    Adresse MAC Destination : 52:0c:c7:1d:ca:35\\n    Adresse MAC Source      : 37:38:1f:55:6b:98\\n    Protocol                : 2048\\n'
    True
    >>> a[1] == 2048
    True
    >>> a[2].decode('utf-8') == "coicoi"
    True
    """
    addrDest = decode_mac(data[0:6]) # on récupère l'adresse de destination
    addrSource = decode_mac(data[6:12]) # et l'adresse source
    protocolType = struct.unpack("!H",data[12:14])[0] # le type de protocole encapsulé
    donnees = data[14:len(data)] # et les données

    return f">>> Trame Ethernet <<<\n    Adresse MAC Destination : {addrDest}\n    Adresse MAC Source      : {addrSource}\n    Protocol                : {protocolType}\n",protocolType,donnees

def decode_trame(data) :
    """
        cette fonction sert a decapsuler une trame Ethernet ; elle fonctionne surtout lorsque la trame contient un protocole IP, puis un protocole TCP, UDP ou ICMP (si ce n'est pas le cas, elle renvoie une erreur potentielle)
    """

    #dictionnaire contenant l'ensemble des fonctions a executer selon l'identifiant numerique du protocole encapsule ;
    protocolID = {2048: lambda data: decode_ip(data), 34525: lambda data: print("IPV6 protocol"), 2054: lambda data: print("ARP protocol"), 1: lambda data: decode_icmp(data), 6: lambda data: decode_tcp(data), 17: lambda data: decode_udp(data)}
    
    etherDecode = decode_Ethernet(data)
    print(etherDecode[0])
    if etherDecode[1] == 2048:
        protocolEnc = protocolID[etherDecode[1]](etherDecode[2])
        print(protocolEnc[0])
        protocolEnc2 = protocolID[protocolEnc[1]](protocolEnc[2])
        if protocolEnc[1] in protocolID:
            if protocolEnc[1] != 1 :
                print(protocolEnc2[0])
                print(protocolEnc2[1].decode('utf-8'))
            else:
                print(protocolEnc2)
        else:
            print(f"attention, le protocole d'identifiant {protocolEnc[1]} n'est pas pris en compte ou n'existe pas")

    else:
        if etherDecode[1] in protocolID:
            protocolID[etherDecode[1]](etherDecode[2])
        else:
            print(f"attention, le protocole d'identifiant {protocolEnc[1]} n'est pas pris en compte ou n'existe pas")

if __name__ == "__main__" :
    doctest.testmod()

    print("ex_complet1 :")
    decode_trame(ex_complet1)
    print("ex_complet2 :")
    decode_trame(ex_complet2)
    print("ex_complet3 :")
    decode_trame(ex_complet3)
    


