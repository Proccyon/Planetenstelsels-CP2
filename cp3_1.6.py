import numpy as np
import matplotlib.pyplot as plt

#Making a figure of the roche limit plotted against the densities of planets
rho_planets = np.arange(0.500, 6.0) #g/cm^3
M_sun = 1.98855E33 #g
R_sun = 6.957E10 #cm
V_sun = (4/3)*np.pi*(R_sun)**3 #cm^3
rho_sun = M_sun / V_sun #g/cm^3
a_roche = 2.456*(rho_planets / rho_sun)**(1/3)

plt.plot(rho_planets, a_roche)
plt.grid()
plt.xlim(np.amin(rho_planets), np.amax(rho_planets))
plt.ylim(np.amin(a_roche), np.amax(a_roche))

plt.title("The value of the Roche limit plotted against the densities of planets around the sun")
plt.ylabel("Value of the Roche limit")
plt.xlabel("Planet densities (g/cm^3)")