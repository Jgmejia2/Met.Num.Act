import numpy as np
import matplotlib.pyplot as plt

f= lambda x: x**2-x+1
g= lambda x: 2/(x-1)

x=np.linspace(-10,10,500)

plt.plot(x,f(x))
plt.plot(x,g(x))
plt.title("Funciones")
plt.grid()