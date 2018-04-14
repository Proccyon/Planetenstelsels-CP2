import Astronomy as As
import matplotlib.pyplot as plt
import numpy as np

#We berekenen de afstand vanaf de aarde tot het massemiddelpunt van aarde-maan



#Opdr 1d

Rc_P = 1 #Afstand planeet tot massa middelpunt in Au
Mzon = As.Sun.M / As.Earth.M #Massa zon in jupiter massas

Mmin = 0.1 #Earth masses
Mmax = 5* As.Jupiter.M / As.Earth.M #maximaal 5 jupiter massas in aardmassas
Bins = 10

Mp = np.linspace(Mmin,Mmax,Bins,dtype="f")
Rc_Zon = Rc_P * (Mp/Mzon) #Afstand zon tot massamiddelpunt in Au


P = As.PeriodKepler(As.Sun.M,Mp*As.Earth.M,(Rc_P+Rc_Zon)*As.AU) #Bereken de omloopstijd via kepler


VSter = (Rc_Zon*As.AU)*np.pi*2 / P #Km/s

plt.plot(Mp,VSter)
plt.ylim(ymin=0)
plt.xlim(xmin=0,xmax=np.amax(Mp))

plt.title("Snelheid van de zon als functie van de massa van een planeet")
plt.xlabel("Massa planeet (Aardmassas)")
plt.ylabel("Snelheid zon (Km/s)")
plt.grid()

plt.show()

