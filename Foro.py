#IMPORTACION DE LIBRERIAS
import numpy as np
import matplotlib.pyplot as plt

#METODO DE BISECCION
def biseccion(f,a,b,tol):
    punto1=a
    m=b
    k=0
    if(f(a)*f(b)>0):
        print("No hay raiz")
    while(abs(punto1-m)>tol):
        punto1=m
        m=(a+b)/2
        if(f(m)*f(a)<0):
            b=m
        if(f(m)*f(b)<0):
            a=m
        print('el intervalo es [',a,',',b,']')
        k=k+1
    print("METODO BISECCION")
    print("LA RAIZ ES IGUAL A ",m," CON ",k," INTERRACION")

#METODO DE NEWTON
def newton(f,df,x0,tol):
    xi=x0
    i=0
    while(abs(xi)>tol):
        i=i+1
        xi=xi-f(xi)/df(xi)
        if abs(f(xi)) < tol:
            print("METODO NEWTON")
            print("LA RAIZ ES IGUAL A ",xi," CON ",i," INTERRACION")
            break
    return None

f= lambda x: x-np.cos(2*x)+np.pi#Funcion del compañero
df= lambda x: 1+2*np.sin(2*x)#funcion derivada para newton
#EJECUCION DE LOS METODOS
biseccion(f,-3,-2,10e-5)
print("")
newton(f,df,-2,10e-5)

x=np.linspace(-10,10,500) #Intervalo de grafico y los puntos
plt.plot(x,f(x))#Grafico f(x)
plt.title("Funciones") #Titulo
plt.grid() #Defino cuadros para mejor compresion del Grafico
plt.show() #Muestro a Pantalla