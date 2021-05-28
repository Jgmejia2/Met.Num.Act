import numpy as np
import matplotlib.pyplot as plt

f= lambda x: np.sin(x)
g= lambda x: np.cos(x)

x=np.linspace(0,10,100)

plt.plot(x,f(x))
plt.plot(x,g(x))
plt.title("Funciones")
plt.grid()