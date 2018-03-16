import numpy as np
import matplotlib.pyplot as plt


#opdr 1.6

Data = np.loadtxt("C:\Users\Eigenaar\Desktop\Uni\Planetenstelsels\CP2\RvData.txt")
Time = Data [:,0] #s
Speed = Data [:,1] #km/s

plt.scatter(Time,Speed,marker=".",s=1,color="black",label="Speed")
plt.axhline(np.average(Speed),0,1,color="red",label="Average speed",linestyle="dashed") #Average speed

plt.title("Time VS Radial velocity of WASP-203")
plt.xlabel("Time(s)")
plt.ylabel("Speed(km/s)")
plt.xlim(xmin=0,xmax = np.amax(Time))
plt.grid()
plt.legend()
plt.show()

#De grafiek laat een sinusachtige golf zien.
#De golf wordt veroorzaakt door draaing van de planeet om zijn ster.
#De data is altijd positief omdat het planetenstelsel van de aarde af beweegt.