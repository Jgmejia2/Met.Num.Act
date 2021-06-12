#Imporatando las librerias
import numpy as np
import matplotlib.pyplot as plt

f= lambda x: x**2-x+1 #Funcion f(x)
g= lambda x: 2/(x-1)  #Funcion g(x)

x=np.linspace(-10,10,500) #Intervalo de grafico y los puntos

plt.plot(x,f(x),label='$x^2-x+1$')#Grafico f(x)
plt.plot(x,g(x),label='$2/(x-1)$')#Grafico g(x)
plt.title("Funciones") #Titulo
plt.grid() #Defino cuadros para mejor compresion del Grafico
plt.legend()#muestra nombre,color de la funcion
plt.show() #Muestro a Pantalla