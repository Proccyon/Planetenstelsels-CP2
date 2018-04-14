import Astronomy as As
import matplotlib.pyplot as plt
import numpy as np

#We berekenen de afstand vanaf de aarde tot het massemiddelpunt van aarde-maan



#Opdr 1b
Mc_Earth_Moon = As.CalcCenterMass(As.Earth.M,As.Moon.M,As.Moon.L)
print "Afstand van aarde tot massamiddelpunt aarde-maan: " +str(Mc_Earth_Moon)+"km"

#Opdr 1c

Rc_P = 1 #Afstand planeet tot massa middelpunt in Au
Mzon = As.Sun.M / As.Earth.M #Massa zon in jupiter massas

Mmin = 0.1 #Earth masses
Mmax = 5* As.Jupiter.M / As.Earth.M
Bins = 10

Mp = np.linspace(Mmin,Mmax,Bins)
Rc_Zon = Rc_P * (Mp/Mzon) * As.AU #Afstand zon tot massamiddelpunt
Rc_Zon = np.round(Rc_Zon,0)

plt.scatter(Mp,Rc_Zon)

Ystretch = 1.1
plt.xlim(xmin=0)
plt.ylim(ymin=0,ymax=np.amax(Rc_Zon)*Ystretch)


plt.title("Halve-lange as van de zon als functie van de massa van een planeet")
plt.xlabel("Massa planeet (Aardmassas)")
plt.ylabel("Halve-lange as zon (Km)")

plt.xticks(Mp)
plt.yticks(Rc_Zon)
plt.ticklabel_format(style="sci",axis="y",scilimits=(0,0))
plt.grid()

plt.show()

