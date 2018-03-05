import numpy as np
import matplotlib.pyplot as plt


#Load data
Data = np.loadtxt("C:\Users\Eigenaar\Desktop\Uni\Planetenstelsels\CP2\Data.dat")
Phase = Data [:,0]
Flux = Data [:,1]

#Calculate average around Phase = 0
Delta_P = 0.005 
TransitPhase = (Phase > -Delta_P) & (Phase < Delta_P)
TransitFlux = Flux[TransitPhase]
AverageFlux = np.average(TransitFlux)
print "Average flux around Phase = 0: " + str(AverageFlux)


#Scatter plot of flux of WASP-203
plt.scatter(Phase,Flux,marker=".",s = 1,color = "black")
plt.title("Relative flux of star WASP-203 VS phase of exoplanet WASP-203b")
plt.xlabel("Phase (0 at transit)")
plt.ylabel("Relative Flux")
plt.xlim(np.amin(Phase),np.amax(Phase))
plt.show()
