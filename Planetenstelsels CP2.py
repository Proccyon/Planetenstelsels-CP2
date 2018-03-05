import numpy as np
import matplotlib.pyplot as plt


# Input: Phase, Flux,Binsize
# Output: Array of Phase and Flux
def BinCurve(phase, flux, binsize):
	bins = 1.0 / binsize
	
	newphase = []
	newflux = []
	x = np.arange(np.min(phase),np.max(phase), binsize)
	for b in x: #bin
		count = 0
		f = []
		for p in range(len(phase)):
			if (phase[p] >= b and phase[p] < b+binsize):
				count = count + 1
				f.append(flux[p])
 
		newphase.append(b + binsize/2)
		g = np.array(f)
		newflux.append(np.mean(g))

	return np.array(newphase),np.array(newflux)




#Load data
Data = np.loadtxt("C:\Users\Eigenaar\Desktop\Uni\Planetenstelsels\CP2\Data.dat")
Phase = Data [:,0]
Flux = Data [:,1]

#Scatter plot of flux of WASP-203
plt.figure(1)
plt.scatter(Phase,Flux,marker=".",s = 1,color = "black")
plt.title("Relative flux of star WASP-203 VS phase of exoplanet WASP-203b")
plt.xlabel("Phase (0 at transit)")
plt.ylabel("Relative Flux")
plt.xlim(np.amin(Phase),np.amax(Phase))
plt.show()


#Scatter plot of flux using bins
plt.figure(2)
BinSize = 0.005
NewPhase, NewFlux = BinCurve(Phase,Flux,BinSize)

plt.plot(NewPhase,NewFlux,color = "firebrick")
plt.scatter(NewPhase,NewFlux,marker=".",color = "black")

plt.title("Relative flux of star WASP-203 VS phase of exoplanet WASP-203b binned")
plt.xlabel("Phase (0 at transit)")
plt.ylabel("Relative Flux")
plt.xlim(-0.1,0.1)
plt.show()

#Calculate average around Phase = 0
Delta_P = 0.005 #Area around Phase(0) that is used
TransitPhase = (Phase > -Delta_P) & (Phase < Delta_P)
TransitFlux = Flux[TransitPhase]
AverageFlux = np.average(TransitFlux)
print "Average flux around Phase(0): " + str(AverageFlux)
#Output: Average flux around Phase(0): 0.949356592986
