#exercice préliminaire

def maxInTab(tab):
    m = tab[0]
    for i in tab[1::]:
        if i > m:
            m = i
    return m

def indiceMax(tab):
    Max = maxInTab(tab)
    for i in range(len(tab)):
        if tab[i] == Max:
            return i

print('exercices préliminaires:')

print("maximum d'une liste")
print("le maximum de la liste {} est {}, d'indice {}".format([1,6,3,7,2], maxInTab([1,6,3,7,2]), indiceMax([1,6,3,7,2])))
print('\n\n')

#exercice 19

def direction(tab):
    betterDir = [[0, 'n'], [0, 'e']]
    for dir in tab:
        if dir[1] == 'n' :
            betterDir[0][0] += dir[0]
        elif dir[1] == 's':
            betterDir[0][0] -= dir[0]
        if dir[1] == 'e' :
            betterDir[1][0] += dir[0]
        elif dir[1] == 'o':
            betterDir[1][0] -= dir[0]

    returnValue = [[], []]
    if betterDir[0][0] < 0:
        returnValue[0] = [betterDir[0][0] * -1, 's']
    elif betterDir[0][0] == 0:
        returnValue.pop(0)
    else:
        returnValue[0] = betterDir[0]
    
    if betterDir[1][0] < 0:
        returnValue[1] = [betterDir[0][0] * -1, 'O']
    elif betterDir[1][0] == 0:
        returnValue.pop(-1)
    else:
        returnValue[1] = betterDir[1]

    return returnValue

print("exercice 19:")
print( direction([[50,'n'], [20,'e'], [30,'s'], [82,'e'], [48,'n'], [43,'o'], [51,'s'], [18,'n'], [46,'e']]))
print('\n\n')

#exercice 20

def stripSpace(str):
    i = 0
    while (str[i] != ' ' and i < len(str)):
        i += 1
    if i == len(str):
        return str
    return (str[i + 1:])    

print('sa main -> {}'.format(stripSpace('sa main')))

def de(part):
    return ('De {}, {}, {}\n'.format(part, stripSpace(part), stripSpace(part)))

def couplet(tabOfPart, i):
    str = "Jean Petit qui danse (bis)\n"
    #for i in range(len(tabOfPart)):
    str += "De {} il danse (bis)\n".format(tabOfPart[i])
    for j in range(i, -1, -1):
        str += de(tabOfPart[j])
    str += 'Ainsi danse Jean Petit.\n'
    return str

def song(tabOfPart):
    str = ""
    for i in range(len(tabOfPart)):
        str += couplet(tabOfPart, i)
        str += '\n'
    return str
print(song(["son doigt", 'sa main', 'ses cheveux']))


#ex 21

def Somme_K(n):
    result = 1/2
    for k in range(2, n+1):
        result += (k**2)/(k**2 + 1)
    return result

def list_n(n):
    tab = []
    for i in range(1,n+1):
        tab.append((n + i)/(n**2 + i**2))
    return tab

def list_k(n):

    for k in range(1, n+1):
        tab = []
        for i in range(1, k+1):
            tab.append((k+i)/(k**2 + i**2))
        print(tab)

def double_somme(n):
    result = 0
    for k in range (1, n+1):
        for i in range(1, k+1):
            result+= (k + i)/(k**2 + i**2)
    return result

print(double_somme(5))

def Gray(n):
    G = [[0], [1]]
    for i in range(n-1):
        L1 = [i[:] for i in G]
        L2 = [i[:] for i in G]