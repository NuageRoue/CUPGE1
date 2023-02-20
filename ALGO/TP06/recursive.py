def triangleBas(n):
    if n > 0:
        print(n * '*')
        triangleBas(n -1)

def sablier(n):
    if n > 0:
        print(n * '*')
        sablier(n - 1)
        if n > 1:
            print((n) * '*')
sablier(5)

def iterSearch(tab, el):
    for elt in tab:
        if elt == el:
            return True
    return False

def recurSearch1(tab, el, i, j):
    if i < j:

        if tab[i] == el:
            return True
        elif tab[i] < el:
            return recurSearch1(tab, el, i + 1, j)
    return False

def recurSearch2(tab, el):
    print(tab)
    if tab != []:

        if tab[0] == el:
            return True
        elif tab[0] < el:
            return recurSearch2(tab[1::], el)
    return False

print(recurSearch2(list(range(19)), 17))


