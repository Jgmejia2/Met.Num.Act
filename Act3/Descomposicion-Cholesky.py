#Importar librerias
import numpy as np
#matriz A del ejercicio
A = np.array([[4, 6, 10.],
              [6, 25, 19],
              [10, 19, 62]])

def cholesky(A):#metodo
    A=np.array(A,float)
    L=np.zeros_like(A)
    n,_=np.shape(A)
    for j in range (n):
        for i in range(j,n):
            if i==j:
                L[i,j]=np.sqrt(A[i,j]-np.sum(L[i,:j]**2))
            else:
                L[i,j]=(A[i,j]-np.sum(L[i,:j]*L[j,:j]))/L[j,j]
    print (L)

cholesky(A)