import Astronomy as As
import matplotlib.pyplot as plt
import numpy as np


def ReadGasList():
    
    Output = np.array([])
    for i in range(len(As.GasList)):
        Output = np.append(Output,As.GasList[i].M)

    return Output


#Opdr2c

MList = ReadGasList()
T=255 #K

for i in range(len(As.GasList)):

    M = As.GasList[i].M
    v,f = As.MaxBolzd(M,T)

    Fmax = np.array([])
    Fmax = np.append(Fmax,np.amax(f))

    Xmax = 2000
    XTicks = np.arange(0,Xmax,200)
    
    plt.plot(v,f,label=As.GasList[i].N)

Fmax = np.amax(Fmax)


Ystretch = 1.2 
plt.xlim(xmin=0,xmax=Xmax)
plt.ylim(ymin=0)

plt.grid()

plt.title("Snelheidsverdeling van N2 met T="+str(T)+"K")
plt.xlabel("v(m/s)")
plt.ylabel("kansverdeling f(v)")

plt.legend()
plt.show()