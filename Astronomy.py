#Constanten

import math
import numpy as np

class Body:
    
    def __init__(self,Name,Radius,Mass,Density,Rotation = None,Distance = None):
        
        self.N = Name
        self.R = Radius #Km
        self.M = Mass #Kg
        self.D = Density #Kg/m^3
        self.T = Rotation #day
        self.L = Distance #Km


def Gravity(R,m1,m2): #Calculates Gravity between 2 objects
    return G * m1 * m2 / (R**2) * 1000 #returns answer in N
    
def Acceleration(R,M): #Calculates Acceleration due to Gravity
    return (G * M / (R**2)) * 1000 #returns answer in m/s^2

def VolumeSphere(R): #Calculates volume of sphere
    return 4 * math.pi * (R**3) / 3
    
def EscapeVelocity(R,M): #Calculates escape velocity
    return math.sqrt(2*M*G/R) #returns anwer in km/s

def CalcCenterMass(m1,m2,r): #Calculates distance of m1 to the center of mass for 2 objects
    return r*m2 / (m1+m2)

def PeriodKepler(M,m,r): #Calculates period of object through keplers third law
    return ((r**3)*(4*np.pi**2) / (G*(M+m)))**0.5
    
def MaxBolzd(m,T):
    v = np.arange(0,30000,1)
    
    Part1 = np.sqrt((m/(2*np.pi*Kb*T))**3)
    Part2 = 4*np.pi*v**2
    Part3 = np.exp((-m*v**2)/(2*Kb*T))
    return v,Part1*Part2*Part3
    
    
G = 6.674E-20 #KN*KM^2*Kg^-2
h = 6.62607004E-34 # m2 kg/s
C = 299792458 #m/s
AU = 149597871 #Km
Par = 3.08567758E13 #Km
Kb = 1.38E-23# J/K
U = 1.660539E-27#kg

Mercury = Body("Mercury",2440,3.30E23,5430,58.6)
Venus = Body("Venus",6052,4.87E24,5240,243)
Earth = Body("Earth",6378,5.97E24,5520,0.99)
Mars = Body("Mars",3397,6.42E23,3930,1.03)
Jupiter = Body("Jupiter",71492,1.90E27,1330,0.41)
Saturn = Body("Saturn",60268,5.68E26,690,0.45)
Uranus = Body("Uranus",25559,8.68E25,1320,0.72)
Neptune = Body("Neptune",24766,1.02E26,1640,0.67)
Pluto = Body("Pluto",1150,1.27E22,2060,6.39)
Moon = Body("Moon",1738,7.35E22,3340,1,384400)
Sun = Body("Sun",695000,1.99E30,1410,24.6)

PlanetList = [Mercury,Venus,Earth,Mars,Jupiter,Saturn,Uranus,Neptune,Pluto]



    