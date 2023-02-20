import math

print(math.sqrt(5))

print(math.exp(3))

print(math.cos(4))

print(math.tan(math.pi/4))

print(math.log(10))

import numpy as np

print(np.zeros(7))
#return an array of given shape and type (if none are given, then float) filled with 0

print(np.ones(6))
#return an array of given size filled with 1

print(np.identity(3))
#return the identity array

print(np.array([3,7,-1,2]))

print(np.array([[3,7],[-1,2]]))
print(np.arange(10,30,5))
print(np.linspace(0,2,9))
print(np.sin(np.linspace(0,2*np.pi,20)))
#math.sin(np.linspace(0,2*np.pi,20))
print("a et b")
a = np.array([[1,3],[0,4]])
b = np.array([[4,0],[-1,1]])
print(a+b)
print(a+4)
print(a*b)
print(3*a)
print(a*3)
print(np.add(a,b))
print(a.dot(b))
print(a @ b)
print(a.transpose())
print(np.linalg.matrix_power(a,2))
print(a.shape)
print(a.sum())
print(a.sum(axis=0))
print(a.sum(axis=1))
print(a.min())
print(a.max())
print(a[1])
print(a[0,1])
print(a[0][1])

def f(x):
    return x * x * np.sin(x) + 4

print(f(np.arange(11)))

