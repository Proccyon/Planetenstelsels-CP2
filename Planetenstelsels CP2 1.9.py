import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import minimize

#opdr 1.9

Data = np.loadtxt("C:\Users\Eigenaar\Desktop\Uni\Planetenstelsels\CP2\RvData.txt")
Time = Data [:,0] #s
Speed = Data [:,1] #km/s

AverageSpeed = np.average(Speed)

plt.scatter(Time,Speed,marker=".",s=1,color="black",label="Speed")
plt.axhline(AverageSpeed,0,1,color="red",label="Average speed",linestyle="dashed") #Average speed

plt.title("Time VS Radial velocity of WASP-203")
plt.xlabel("Time(s)")
plt.ylabel("Speed(km/s)")
plt.xlim(xmin=0,xmax = np.amax(Time))

Ystretch = 0.3 #How much the graph is stretched in y direction

Ymin = np.amin(Speed) - Ystretch*(np.amax(Speed) - np.amin(Speed))
Ymax = np.amax(Speed) + Ystretch*(np.amax(Speed) - np.amin(Speed))
plt.ylim(ymin=Ymin,ymax = Ymax)
plt.grid()


#Function for a sinewave
def Sine(K,Phi,P,K0,Time):
    return K*np.sin(2*np.pi*(Time)/P+Phi) + K0
    

#Fits data with a theoretical fit
def FitFunction(Var,Time,Vmes):
    K = Var[0]
    Phi = Var[1]
    P = Var[2]
    K0 = Var[3]
    Vfit = Sine(K,Phi,P,K0,Time)
    return np.sum((Vmes-Vfit) ** 2)

#guesses
K0_g = AverageSpeed
K_g = np.amax(Speed) - K0_g
P_g = 160714
Phi_g = -3

#Plot of guess
VGuess = Sine(K_g,Phi_g,P_g,K0_g,Time)
plt.plot(Time,VGuess,color="green",label="Guessed Sine")


x0 = np.array([K_g,Phi_g,P_g,K0_g])

#Minimize error
x = minimize(FitFunction,x0, args=(Time,Speed),method="powell").x

K = x[0]
Phi = x[1]
P = x[2]
K0 = x[3]

#Plot of found values
Vminimize = Sine(K,Phi,P,K0,Time)
plt.plot(Time,Vminimize,color="blue",label="Fitted Sine")

plt.legend(fontsize = 7,loc="lower right")
plt.show()