#importacion de la libreria
import numpy as np

#Ingreso valor en cada posicion de la matriz
a= int(input("Inserte un numero en la posicion [0,0]: "))
b= int(input("Inserte un numero en la posicion [0,1]: "))
c= int(input("Inserte un numero en la posicion [1,0]: "))
d= int(input("Inserte un numero en la posicion [1,1]: "))

M = np.matrix([[a, b],[c, d]])
print("\nLa matriz original es: ")
print(M)
print("\nLa matriz inversa es: ")
try:
    MI= np.linalg.inv(M) #metodo matriz inversa
except np.linalg.LinAlgError:
    print("No tiene M.I")
else:    
    print(MI)