import numpy as np
import matplotlib.pyplot as plt

Data = np.loadtxt("C:\Users\Eigenaar\Desktop\Uni\Planetenstelsels\CP2\Data.dat")
Phase = Data [:,0]
Flux = Data [:,1]

plt.scatter(Phase,Flux,marker=".",s = 1,color = "black")
plt.title("Relative flux of star WASP-203 VS phase of exoplanet WASP-203b")
plt.xlabel("Phase (0 at transit)")
plt.ylabel("Relative Flux")
plt.xlim(np.amin(Phase),np.amax(Phase))
plt.show()
