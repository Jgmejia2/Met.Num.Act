#Importar librerias
import numpy as np
#matrices del ejecicio
A = np.array([[7, 1, -1, 2],
              [1, 8, 0, -2],
              [-1, 0, 4, -1],
              [2, -2, -1, 6]])
b = np.array([3, -5, 4, -3])
#Metodo SOR
def SOR (A,b,w):
    print()
    print("__________METODO DE SOR__________\n")
    n=np.size(b)
    D=np.eye(n)#matriz Diagonal
    D[np.arange(n),np.arange(n)]=A[np.arange(n),np.arange(n)]
    x=np.zeros(n)#matriz inicial 
    print("Iteracion 0: ",x," Matriz inical")
    L_U=D-A#matriz triangular inferior + superior
    L=np.tril(L_U)#matriz triangular inferior
    U=np.triu(L_U)#matriz triangular superior
    for i in range (5):
        #formula de SOR
        x=np.dot(np.dot(np.linalg.inv(D-w*L),(1-w)*D+w*U),x)+w*np.dot(np.linalg.inv(D-w*L),b)
        print("Iteracion ",i+1," el resultado es: ", x.round(decimals=4))
    print("Comprobación ",np.dot(A,x)-b)
    xR = ([1,-1,1,-1])
    e = np.zeros(4)
    for i in range(4):
        e[i] = (xR[i]-x[i])/xR[i]
        print('El error de x',i+1,'es =',100*abs(e[i]),'%')

SOR(A,b,1.1)