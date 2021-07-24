#Importar librerias
import numpy as np
#matrices del ejecicio
A = np.array([[7, 1, -1, 2],
              [1, 8, 0, -2],
              [-1, 0, 4, -1],
              [2, -2, -1, 6]])
b = np.array([3, -5, 4, -3])
#Metodo Jacabi
def jacobi (A,b):
    print()
    print("__________METODO DE JACOBI__________\n")
    n=np.size(b)
    D=np.zeros((n,n))#matriz Diagonal
    x=np.zeros(n)#matriz inicial 
    print("Iteracion 0: ",x," Matriz inical")
    for i in range(0,n):
        for j in range (0,n):
            if (i==j):
                D[i,j]=A[i,j]
    D_inv=np.linalg.inv(D)
    L_U=D-A#matriz triangular inferior + superior
    for a in range (15):
        #formula de Jacobi
        x=np.dot(np.dot(D_inv,L_U),x)+np.dot(D_inv,b)
        print("Iteracion ",a+1," el resultado es: ", x.round(decimals=4))
    print("Comprobación ",np.dot(A,x)-b)
    xR = ([1,-1,1,-1])
    e = np.zeros(4)
    for i in range(4):
        e[i] = (xR[i]-x[i])/xR[i]
        print('El error de x',i+1,'es =',100*abs(e[i]),'%')

jacobi(A,b)