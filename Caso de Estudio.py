import numpy as np
#ENTRADAS
n=100
a=np.ones(99)/2             #a=Vector subdiagonal
d=np.ones(n)                #d=Vector diagonal
c=np.ones(99)/2             #c=Vector superdiagonal
b=np.ones(100)+np.ones(100) #b=Vector Terminos Independientes
b[0],b[99]=1.5,1.5
#SALIDA
#Vector Solucion
def tridiag(n,d,a,c,b):
    x = np.zeros(n)
    #Eliminacion directa
    for i in range(1,n-1):
        mult = a[i-1]/d[i-1]
        d[i] -= mult*c[i-1]
        b[i] -= mult*b[i-1]
    print(d)
    print(b)
    #sustitucion regresiva
    x[n-1] = b[n-1]/d[n-1]
    for i in range(n-2,-1,-1):
        x[i] = (b[i]-c[i]*x[i+1])/d[i]
    print(x)
    return x
    
tridiag(n,d,a,c,b)