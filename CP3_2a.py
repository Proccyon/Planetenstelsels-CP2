import Astronomy as As
import matplotlib.pyplot as plt
import numpy as np

#Opdr2b

M = 28.014*As.U #kg
T=300 #K

v,f = As.MaxBolzd(M,T)

Vmax = v[np.argmax(f)]
Fmax = np.amax(f)

Ystretch = 1.2 
Xmax = 1200
XTicks = np.arange(0,Xmax,200)
XTicks = np.append(XTicks,Vmax)

plt.plot(v,f)
plt.axvline(Vmax,ymax=1/Ystretch,color = "red",linestyle="--")




plt.xlim(xmin=0,xmax=Xmax)
plt.ylim(ymin=0,ymax=Fmax*Ystretch)
plt.xticks(XTicks)
plt.grid()

plt.title("Snelheidsverdeling van N2 met T=300")
plt.xlabel("v(m/s)")
plt.ylabel("kansverdeling f(v)")

plt.show()