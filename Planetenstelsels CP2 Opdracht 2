#Calculating semi-major axis
P_planet = 156569.441613 #s
G = 6.67*(10)**(-11) #m^3*s^(-2)*kg^(-1)
M_star = 0.80*1.989*(10)**30 #kg
SM_Axis = (((P_planet**2)*G*M_star)/((2*np.pi)**2))**(1/3)
#Output SM_Axis: 4039258283.2208753 m

#Calculating inclination plus the mass of the planet
RadiusSum = (RadiusStar + RadiusPlanet)*6.957*(10)**8
inclination = math.degrees(np.arccos(RadiusSum / SM_Axis))
#Output inclination: 80.6499565021097 degrees

Observed_vstar = 9.34230208046*(10)**3 # m/s
vstar = Observed_vstar / np.sin(math.radians(inclination))
#Output vstar: 9468.093356802636 m/s 

M_planet = vstar*(M_star)**(2/3)*((2*np.pi*G)/(P_planet))**(-1/3)
#Output M_planet: 9.294217077181486e+28 kg

#Density calculation
V_planet = (4/3)*np.pi*(RadiusPlanet*6.957*(10)**8)**3
Density_planet = M_planet / (V_planet)
#Output Density_planet: 12664.896481299162 kg/m^3

#Plot of Effective Temperature planet against Albedo
L_star = 0.490*3.828*(10)**26
A_planet = 0.34
sigma = 5.670373*(10)**(-8) #W*m^(-2)*K^(-4)
A = np.arange(0.0, 1.01, 0.01)

plt.plot(A, ((L_star*(1-A))/(16*np.pi*sigma*(SM_Axis)**2))**(1/4), marker=".", color = "black")
plt.title("Plot of Effective Temperature planet against Albedo")
plt.xlabel("Albedo going from 0 to 1")
plt.ylabel("Effective Temperature in Kelvin")
plt.xlim(np.amin(A), np.amax(A))

#Effective Temperature of planet at A=0.34
T_eff = ((L_star*(1-A_planet))/(16*np.pi*sigma*(SM_Axis)**2))**(1/4)
#Output T_eff = 1277.3408554938808 K
