#Importamos las librerias
import numpy as np
import math as mt

#mensaje del programa
print("Serie de Taylor de Sen(pi/3)\t hasta el 50:\n\n")

x=np.pi/3#valor de x para la serie
conteoT= 0#incicializador para el conteo de Taylor

#Serie de Taylor de Sen(pi/3) hasta 50
for i in range (1,51):
    conteoT=conteoT+(-1)**(i+1)*x**(2*i-1)/mt.factorial(2*i-1)
    print(i,"\t",conteoT)