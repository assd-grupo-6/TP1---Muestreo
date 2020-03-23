import matplotlib.pyplot as plt
import numpy as np
import math

# Frecuencia central de la cuadrada
fc = 3e3
T = 1/fc

# Frecuencia de nuestro oscilador
fs = 100e3

t = np.linspace(0, 1*T, 1000)
x= np.zeros(len(t))

# Numero maximo de harmonicos que pueden ser sampleados por la fs
Nmax = int((1/2)*(fs/(2*fc) + 1))


for i in range(1,Nmax):
    xi=[]
    for ti in t:
        xi.append(math.sin(2*(math.pi)*(2*i-1)*fc*ti)*4/math.pi/(2*i-1))
    for j in range(len(x)):
        x[j] = x[j] + xi[j]
plt.plot(t,x)

print("Number of harmonics that chan be sampled = " + str(Nmax))
# Frecuencia maxima de sampleo necesaria para samplear los Nmax armonicos
max_freq = (2*Nmax-1)*fc/1e3
print("Min sampling freq needed = " + str(max_freq) + "kHz")

plt.show()