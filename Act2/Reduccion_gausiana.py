import numpy as np
# Creamos la matriz de valores
A = np.array([[4., -1., -1., 0.],
              [-1., 4., 0., -1.],
              [-1., 0., 4., -1.],
              [0., -1., -1., 4.]])
B = np.array([30., 60., 40., 70.])

def EliminacionGsussiana (A,B):
    A2=np.copy(A)
    B2=np.copy(B)
    print("")
    print("-------------------------------------------")
    print("MÉTODO DE ELIMINICIÓN GAUSSIANA SIN PIVOTEO")
    print("")
    n=len(B)
    for k in range(0,n-1):
        for i in range(k+1,n):
            mult= A[i,k]/A[k,k]
            for j in range(k,n):
                A[i,j]-=mult*A[k,j]
            B[i] -=mult*B[k]
    x=np.zeros(n)        
    x[n-1]=B[n-1]/A[n-1,n-1]
    ## DECLARAMOS VARIABLE x
    print("Las matrices originnales son: ")
    print(A2)
    print(B2)
    print("")
    print("Las nuevas matrices son: ")
    print(A)
    print(B)
    for i in range(n-2,-1,-1):
        suma_j=0
        for j in range(i+1,n):
            suma_j += A[i,j]*x[j]
            #Algoritmo solucion
            x[i]=(B[i]-suma_j)/A[i,i]
    print("")
    print("Los resulatdos de son: ")
    print(x)
    C=np.dot(A, x)-B
    print("El residuo es: ", C)

EliminacionGsussiana(A,B)