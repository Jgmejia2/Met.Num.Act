#Importar librerias
import numpy as np
#Matriz A
A = np.array([[6, 0, 0, 0.],
              [3, 6, 0, 0],
              [4, -2, 7, 0],
              [5, -3, 9, 21]])

def desLU (A):#Descomposiscion LU
    n=int(np.sqrt(np.size(A)))
    L=np.zeros([n,n])
    U=np.copy(A)
    for i in range (0,n):
        for j in range (0,n):
            if (i==j):
                L[i,j]=1
            if (i<j):
                factor = (A[j,i]/A[i,i])
                L[j,i] = factor#Matriz L
                for k in range (0,n):
                    A[j,k]= A[j,k]-(factor*A[i,k])
                    U[j,k]= A[j,k]#Matriz U
    print("---------Descomposicion LU---------")
    print("La matriz L es: \n", L)
    print("La matriz U es: \n", U)

desLU(A)