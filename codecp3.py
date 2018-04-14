import numpy as np
import matplotlib.pyplot as plt
from scipy import integrate

sigma = 5.670373*(10)**(-8) #W*m^(-2)*K^(-4)
G = 6.67E-11 #m^3*s^(-2)*kg^(-1)
Kb = 1.38E-23 # J/K

#Assigment 2.3
def Eff_Temp (Albedo, L_star, SM_axis): 
    base = (L_star*(1-Albedo))/(16*np.pi*sigma*(SM_axis)**2)    
    return (base)**(1/4)

#Calculating Absolute Temperature for the Earth
Albedo_E = 0.3
L_sun = 3.828*(10)**26 #W
SM_axis_E = 1.496*(10)**11 #m  

Temp_E = Eff_Temp(Albedo_E, L_sun, SM_axis_E) 
print(Temp_E)
#254.58412831606898 K

#Determining het amount H2 molecules in the atmosphere of the Earth
m_atmos = 3*10**18 #kg 
frac_H2 = 0.5*10**(-6) #kg/kg or (m^3)/(m^3)
m_atmos_H2 = m_atmos * frac_H2 #kg
m_H2 = 1.6737236*10**(-27) # kg 
amount_H2 = m_atmos_H2 / m_H2 #H2 molecules
print(amount_H2)
#Result: 8.962053232684297e+38 H2 molecules

#Calculating escape velocity for Earth
def EscapeVelocity(R,M): #Calculates escape velocity
    return np.sqrt(2*M*G/R) #returns anwer in km/s

R_E = 6.371E6 #m
M_E = 5.972E24 #kg
v_E = EscapeVelocity(R_E, M_E) #m/s
v_H2 = 0.8 * v_E #m/s
print(v_H2)
#Result: 8945.899167403879 m/s
