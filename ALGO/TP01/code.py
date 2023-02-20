#ex2

def g(x):
	if x < 0:
		return -x**2
	return x**2

def h(x):
	for i in range(x+1):
		if not i%7:
			print(i)

print("exercice 2 :")
print("g(5) = {}".format(g(5)))
print("g(-2) = {}".format(g(-2)))
print('\n')
h(70)
print('\n\n\n')


#ex3 : Xor
def xor(arg1, arg2):
	return ((arg1 and not arg2) or (arg2 and not arg1))

print('exercice 3, ou exclusif')
print("1 et 0 : {} \n0 et 1 : {} \n0 et 0 : {} \n1 et 1 : {} \n".format(xor(1,0), xor(0,1), xor(0,0), xor(1,1)))
print('\n\n\n')


#ex04

#programme a:
#on a une division par 0 (a%0)

#programme b:
#assignation avec un égal de comparaison (==)


#ex05
# le programme affiche 4 car a n'est pas nul, a est une chaine de caractère 
print('exercice 5')
a = 'False'
b = ''
print("a = '{}' \nb = '{}'".format(a,b))
if a:
	print("a n'est pas nul")
if not b:
	print("b est nul")
print('\n\n\n')


#ex06
def isOdd(n):
	if (n%2):
		print('{} est impair'.format(n))
	else:
		print('{} est pair'.format(n))

print('exercice 6')
isOdd(46)
isOdd(47)
print('\n\n\n')


#ex07
def modThree(n):
	res = 0
	if not n%3:
		res = 1
	return res

print('exercice 7')
print(modThree(15))
print(modThree(19))
print('\n\n\n')


#ex8.1
def calcul_impot_1(revenu):
	if revenu > 5875:
		return 0.055 * (revenu - 5875)
	return 0

print('exercice 8.1')
print(calcul_impot_1(5875))
print(calcul_impot_1(5875+100))
print('\n')

#8.2
def calcul_impot_2(revenu):
	if revenu < 5875:
			return 0
	elif revenu < 11720:
		return 0.055 * (revenu - 5875)
	return 0.14 * revenu - 1319.33

print('exercice 8.3')
print('pour un revenu de 3000 euros, l\'impot est de {}\n'.format(calcul_impot_2(3000)))
print('pour un revenu de 7000 euros, l\'impot est de {}\n'.format(calcul_impot_2(7000)))
print('pour un revenu de 20 000 euros, l\'impot est de {}\n'.format(calcul_impot_2(20000)))
print('\n')

#8.4
def calcul_impot_3(revenu):
	if revenu > 11720:
		return 0.14 * revenu - 1319.33
	return calcul_impot_1(revenu)

print('exercice 8.4')
print('pour un revenu de 3000 euros, l\'impot est de {}\n'.format(calcul_impot_3(3000)))
print('pour un revenu de 7000 euros, l\'impot est de {}\n'.format(calcul_impot_3(7000)))
print('pour un revenu de 20 000 euros, l\'impot est de {}\n'.format(calcul_impot_3(20000)))
print('\n')

#8.5
def calcul_impot_4(revenu):
	if revenu > 69783:
		return 0.4 * revenu - 12462.43
	elif revenu >= 26030:
		return 0.3 * revenu - 5484.13
	return calcul_impot_3(revenu)

#8.6
def calcul_impot_mars(revenu, cratere):
	if revenu < 4800:
		return 0.12 * revenu if cratere else 0
	return 0.25 * revenu - 624 if cratere else 0.12 * revenu - 576

print('exercice 8.6')
print("un martien habitant un cratere et touchant un revenu de 4 000 doit payer {} \n".format(calcul_impot_mars(4000, True)))
print("un martien habitant un cratere et touchant 6 000 doit payer {}\n".format(calcul_impot_mars(6000, True)))
print("un martien n’habitant pas de cratere et touchant 6 000 doit payer {}\n".format(calcul_impot_mars(6000, False)))
print('\n\n\n')


#exercice 9:
s = 0
print('sans indenter print :')
for i in range (1, 11) :
	s += 1/i
print (s)
print('\n')

s = 0
print('en indentant print:')
for i in range (1, 11) :
	s += 1/i
	print (s)
print('\n\n\n')


#ex10
def somme_S(n):
	k = 0
	s = 0.0
	while k < n:
		k += 1
		s += 1/k
	return s

print('exercice 10 :')
print('S(10) = {}'.format(somme_S(10)))
print('\n')
#en remplacant < par <=, on aurait obtenu s(n+1)

def produit_H(n):
	k = 2
	s = 1
	if n < 2:
		return -1
	while k <= n:
		s *= 1 - 1/k**2
		k += 1
	return s

print('exercice 10.5')
print('H(5) = {}'.format(produit_H(5)))
print('\n')

def min_S(val):
	n = 0
	s = 0.0
	while s < val:
		n += 1
		s += 1/n
	return n

print('exercice 10.6')
print('le plus petit entier n tel que S(n) est inferieur a 10 est {}'.format(min_S(10)))
print('\n\n\n')


#ex11
def calcul_u(n):
	u = 0
	while n > 0:
		n -= 1
		u = (6+u)/(6-u)
	return u

print('exercice 11.1')
print('u5 = {}'.format(calcul_u(5)))
print('\n')

# avec n >=, on renvoie U(n+1)
# avec n < 0, on renvoie 0

def somme_u(k):
	u = 0
	while k:
		u += calcul_u(k)
		k -= 1
	return u
print('exercice 11.2')
print(somme_u(5))
print('\n\n\n')


#exercice 12
def equipeVS(n):
	tabTeam = [ i for i in range(1, n+1)]
	for team1 in tabTeam:
		for team2 in tabTeam:
			if team1 != team2:
				print("l'équipe {} se déplace contre l'équipe {}".format(team1, team2))
		print('\n')
print('exercice 12 :')
equipeVS(3)
print('\n')

def teamVS(n):
	tabTeam = [i for i in range(1, n+1)]
	for team1 in tabTeam:
		print("Matchs de l'equipe {}".format(team1))
		for i in range(team1):
			if i and i != team1:
				print("l'equipe {} joue contre l'equipe {}".format(team1, i))
		print('\n')
teamVS(4)
print('\n\n\n')


#ex13
def somme3And5(n):
	s = 0
	for k in range(1, n):
		if not(k % 3 and k % 5):
			s += k
	return s
print('exercice 13:')
print('la somme des entiers k compris entre 1 (inclu) et 1000 (exclu) est de {}'.format(somme3And5(1000)))
print('\n\n\n')

#exercice 14

def getAWithB(a,b):
	"""
		renvoie un triplet de valeurs hypothetiques de A en se basant sur B : 
		si B = A1 + A2 + A3 , alors A1 = B - A2 - A3
		etc. 
	"""
	AWithB = [b,b,b]
	for i in range(len(a)):
		for j in range(len(a)):
			if j != i:
				AWithB[i] -= a[j]
	return AWithB

def getAWithC(a, c):
	"""
		renvoie un triplet de valeurs hypothetiques de A en se basant sur B : 
		si B = A1 + A2 + A3 , alors A1 = B - A2 - A3
		etc. 
	"""
	AWithC = [c,c,c]
	for i in range(len(a)):
		for j in range(len(a)):
			if j != i:
				AWithC[i] -= a[j] * (j+1)
	for i in range(len(AWithC)):
		AWithC[i] //= i + 1
	return AWithC

def check(a,b,c, i):
	AWithB = getAWithB(a,b)
	AWithC = getAWithC(a,c)
	
	if AWithB[i] != AWithC[i]:
		return 1
	a[i] = AWithB[i]
	CWithA = a[0] + 2 * a[1] + 3 * a[2]
	return not (sum(a) == b and CWithA == c) 

def getCorrectA(a,b,c):
	AWithB = getAWithB(a,b)
	AWithC = getAWithC(a,c)
	i = 0
	while check(a[::],b,c, i): #AWithB[i] != AWithC[i] and check(a[::],b,c, AWithB[i], i):
		i += 1
	print("a{} n'a pas la bonne valeur; il devrait être {} et pas {}".format(i+1, AWithB[i], a[i]))
	a[i] = AWithB[i]
	return a

def showError(a,b,c):
	"""
		fonction renvoyant 1 si l'erreur se trouve dans l'un des trois A ou 0 si elle se trouve dans B ou C
	"""
	#if a != getAWithC(a,c) and a != getAWithB(a,b):
	CWithA = a[0] + 2 * a[1] + 3 * a[2]
	if sum(a) != b and CWithA != c:
		return (getCorrectA(a,b,c), b, c)
	elif sum(a) != b: #l'erreur est dans b:
		print("b n'a pas la bonne valeur; il devrait être {} et pas {}".format(sum(a),b))
		return (a, sum(a), c)
	elif CWithA != c:
		print("c n'a pas la bonne valeur; il devrait être {} et pas {}".format(CWithA, c))
		return (a, b, CWithA)
	elif sum(a) == b and CWithA == c:
		print("il n'y a pas d'erreur")
		return (a,b,c)
	return -1

print('exercice 14:')
print(showError([3,2,6], 6, 25), end='\n\n')
print(showError([3,1,6], 11, 25), end='\n\n')
print(showError([3,2,5], 11, 25), end='\n\n')
print(showError([3,2,6], 11, 25), end='\n\n')
print(showError([3,2,6], 11, 26))
print('\n\n\n')



#ex15

def inGrid(c):
	return (ord(c[0]) > ord('H') or ord(c[0]) < ord('A')) or (ord(c[1]) > ord('1') or ord(c[1] > ord('9')))

def deplacement_possible(c1, c2):
	if not inGrid(c1) or not inGrid(c2):
		return False
	if c2 == chr(ord(c1[0])+1) + chr(ord(c1[1]) + 2):
		return True
	
	if c2 == chr(ord(c1[0])+1) + chr(ord(c1[1]) - 2):
		return True

	if c2 == chr(ord(c1[0])-1) + chr(ord(c1[1]) + 2):
		return True

	if c2 == chr(ord(c1[0])-1) + chr(ord(c1[1]) - 2):
		return True

	if c2 == chr(ord(c1[0])+2) + chr(ord(c1[1]) + 1):
		return True

	if c2 == chr(ord(c1[0])+2) + chr(ord(c1[1]) - 1):
		return True

	if c2 == chr(ord(c1[0])-2) + chr(ord(c1[1]) + 1):
		return True
	
	if c2 == chr(ord(c1[0])-2) + chr(ord(c1[1]) - 1):
		return True
	
	return False


	
print(deplacement_possible('F4', 'G2'))

#ex16

def binomial(n,k):
	if n == 0:
		return 0
	if k == 0:
		return 1
	return ((n)/(k)) * binomial(n-1, k-1)

print(binomial(15,10))

#ex17

print('exercice 17:')

#n = 2

def tri(n):
	return (n**2 + n)//2

def penta(n):
	return tri(n) + 2 * tri(n - 1)

def hexa(n):
	return penta(n) + tri(n - 1)

# H(n) = T(2n - 1)
# P(n) = T(3n-1)/3

# pour chaque nombre triangulaire de rang de la forme 3n-1, on vérifie si le quotient est un nombre triangulaire impair

def isTri(n):
	i = 1
	while tri(i) <= n:
		if tri(i) == n :
			print('i', i)
			return i
		i += 1
	return -1

def isHexa(n):
	i = 1
	while hexa(i) <= n:
		if hexa(i) == n :
			return True
		i += 1
	return False

def isPenta(n):
	i = 1
	while penta(i) <= n:
		if penta(i) == n :
			return True
		i += 1
	return False


i = 1
notFound = True
while notFound:
	i += 2#2
	rang = isTri(tri(3 * i - 1) // 3)
	print(rang)
	if rang > 0 and rang % 2 == 1 :
		print(tri(rang))
		notFound = False


#exercice 18:

def nbSquare(L, C):
	return ((L*(L + 1)) * (C*(C + 1))) / 4

def ABS(x):
	return x * ((x > 0)-(x < 0))


def nearestSquaredGrid(nb_square):
	C = 1
	while(nbSquare(C, C) < nb_square):
		C += 1
	if ABS(nbSquare(C - 1, C - 1) - nb_square) < ABS(nbSquare(C, C) - nb_square):
		print('on a une grille de dimension {}x{}'.format(C - 1, C - 1))
		return (C - 1)
	print('on a une grid de dimension {}x{}'.format(C, C))
	return (C + 1)

print('\n\n\n')
#print(i)