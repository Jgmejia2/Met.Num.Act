#IMPORTACION DE LIBRERIAS
import numpy as np

#Sustirucion regresiva
def Sus_regre (A, b):
    n=np.size(b)
    x=np.array([0.001,0.001,0.001])
    for i in range (n-1,-1,-1):
        sumj=0
        for j in range (i+1, n):
            sumj += A[i,j]*x[j]
        #Algoritmo de resolucion  
        x[i]=(b[i]-sumj)/A[i,i]
    print("Los resulatdos de ")
    print('x\N{SUBSCRIPT ONE},', 'x\N{SUBSCRIPT TWO},','x\N{SUBSCRIPT THREE}'," son:")
    print(x)

A=np.array([[1,2,-2],[0,1,-1],[0,0,1]])
b=np.array([5,2,0])

Sus_regre (A, b)