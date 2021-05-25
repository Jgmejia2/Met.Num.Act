#importacion de la libreria
import numpy as np

#Ingreso valor en cada posicion de la matrix
a= int(input("Inserte un numero en la posicion [0,0]: "))
b= int(input("Inserte un numero en la posicion [0,1]: "))
c= int(input("Inserte un numero en la posicion [1,0]: "))
d= int(input("Inserte un numero en la posicion [1,1]: "))

M = np.matrix([[a, b],[c, d]])
print(M)
print("La matriz inversa es: ")
MI= np.linalg.inv(M)
print(MI)