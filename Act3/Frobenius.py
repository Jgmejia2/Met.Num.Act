import numpy as np
from math import sqrt

# MATRIZ A REALIZAR (A):
from math import sqrt
A=np.array([[6,1,4],[1,3,8],[2,5,-7]])
m=A.shape[0] # Numero de filas
n=A.shape[1] #numero de columnas
sum_raiz=0
for i in range(m):
    for j in range(n):
            sum_raiz+=A[i][j]**2
    Solucion=sqrt(sum_raiz)
print("-----------------------------------------------------------\n")
print ("Matriz con ",m ,"numero de filas y ",n," numero de columnas")
print("La norma Frobenius es : ",round(Solucion,5))
print("-----------------------------------------------------------")