import numpy as np
import matplotlib.pyplot as plt

sigma = 5.670373*(10)**(-8) #W*m^(-2)*K^(-4)

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
