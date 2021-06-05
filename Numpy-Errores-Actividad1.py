#importacion de la libreria
import numpy as np

#Ingreso valor en cada posicion de la matriz
#Se coloca a cada entrada un int para comvertir el valor
try:
    a= int(input("Inserte un numero en la posicion [0,0]: "))
    b= int(input("Inserte un numero en la posicion [0,1]: "))
    c= int(input("Inserte un numero en la posicion [1,0]: "))
    d= int(input("Inserte un numero en la posicion [1,1]: "))

    M = np.matrix([[a, b],[c, d]])#Adjunta los datos de la matriz
    print("\nLa matriz original es: ")
    print(M)#Muestra la Matriz
    print("\nLa matriz inversa es: ")
    MI= np.linalg.inv(M) #metodo matriz inversa
except ValueError:
    print("Error")
except np.linalg.LinAlgError:#Captura excepcion, si la tiene
    print("No tiene M.I")
else:    
    print(MI)#Imprime la matriz inversa