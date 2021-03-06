# -*- coding: utf-8 -*-
"""
Created on Mon Nov  6 02:56:18 2017

@author: Steven Li
"""

import numpy as np
import matplotlib.pyplot as plt

#----------------------------------------------------------------------------#
# Star Class Creation
#----------------------------------------------------------------------------#

#12 Types of Stars:
'''
    Hypergiant
    Supergiant
    Bright giants
    Giants
    Subgiants
    Main Sequence Dwarfs
    Sub - dwarfs
    Red - giants
    Red - dwarfs
    Brown - dwarfs
    White - dwarfs
    Black - dwarfs (Dead Star)
'''
#Possibly will have multiple classes of stars and change them to specific classes
#when
#specific parameters have been met to keep track of current star type throughout
#calculations.

class Star:
    
    def __init__ ( self , mass , luminosity , radius , temperature ):
        self.mass = mass
        self.lum = luminosity
        self.radius = radius
        self.temp = temperature
        self.spectralClass = spectral(self)
        self.absoMag = boloMag(self)
        self.starType = categorize(self)
        
    def setStar(self):
        self.type = categorize()
        
    def setSpectralClass(self):
        self.spectralClass = spectral()
        
    def getSpectral(self):
        return self.spectralClass
        
    def getMass(self):
        return self.mass
    
    def getLum(self):
        return self.lum
    
    def getRadius(self):
        return self.radius
    
    def getTemp(self):
        return self.temp
    
    def getAbso(self):
        return self.absoMag
    
    def __str__(self):
        return 'Spectral Class: ' + str(self.spectralClass) + '\nAbsolute Magnitude: ' + str(self.absoMag) + '\nStar Type: ' + str(self.starType)
    
#Based on Mass, Luminosity, Radius, and Temperature. Attempt to identify
#what category the star fits into and determine its lifetime(if not already done).
#Then stimulate the evolution of the star. Assuming that the star is singular and
#receives no outside influence such as gaining mass from other stars during its
#collapse. This also assumes that the stars are black bodies in thermal equilibrium.
#Possible outcomes of stellar evolution evolution: Supernova into Neutron Star/Black Hole
#or into a black-dwarf eventually or become a planetary nebula.

#----------------------------------------------------------------------------#
# Categorizing Star in H-R Diagram
#----------------------------------------------------------------------------#

def spectral(Star):
    '''
    Categorize star into it's respective stellar classification    
    '''
    if(Star.getTemp() >= 30000):
        return 'O'
    elif(Star.getTemp() >= 10000):
        return 'B'
    elif(Star.getTemp() >= 7500):
        return 'A'
    elif(Star.getTemp() >= 6000):
        return 'F'
    elif(Star.getTemp() >= 5200):
        return 'B'
    elif(Star.getTemp() >= 3700):
        return 'K'
    elif(Star.getTemp() >= 2400):
        return 'M'
    elif(Star.getTemp() >= 1300):
        return 'L'
    elif(Star.getTemp() >= 550):
        return 'T'
    
def boloMag(Star):
    solarLum = 3.828e26
    return -2.5*np.log10(Star.getLum()*solarLum) + 71.197425
    
def categorize(Star):
    
    #Spectral Type O Categorization
    if(Star.getSpectral() == 'O'):
        if(Star.getAbso() >= 8 and Star.getAbso() <= 11):
            return 'White Dwarfs'
        elif(Star.getAbso() <= 0 and Star.getAbso() >= -4 ):
            return 'Main Sequence'
        elif(Star.getAbso() <= -4 and Star.getAbso() >= -5):
            return 'Giants'
        elif(Star.getAbso() <= -5 and Star.getAbso() >= -6):
            return 'Bright Giants'
        elif(Star.getAbso() <= -6 and Star.getAbso() >= -7):
            return 'Supergiants'
        elif(Star.getAbso() <= -7):
            return 'Hypergiants'
       
    #Spectral Type B Categorization:
    elif(Star.getSpectral() == 'B'):
        if(Star.getAbso() >= 9 and Star.getAbso() <= 13):
            return 'White Dwarfs'
        elif(Star.getAbso() <= 2 and Star.getAbso() >= -3 ):
            return'Main Sequence'
        elif(Star.getAbso() <= -3 and Star.getAbso() >= -4):
            return 'Giants'
        elif(Star.getAbso() <= -4 and Star.getAbso() >= -6):
            return 'Bright Giants'
        elif(Star.getAbso() <= -6 and Star.getAbso() >= -7):
            return 'Supergiants'
        elif(Star.getAbso() <= -7):
            return 'Hypergiants'
        
    #Spectral Type A Categorization:
    elif(Star.getSpectral() == 'A'):
        if(Star.getAbso() >= 10 and Star.getAbso() <= 14):
            return 'White Dwarfs'
        elif(Star.getAbso() < 4 and Star.getAbso() >= 2):
            return 'Main Sequence'
        elif(Star.getAbso() < 2 and Star.getAbso() >= 0):
            return 'Subgiants'
        elif(Star.getAbso() < 0 and Star.getAbso() >= -3):
            return 'Giants'
        elif(Star.getAbso() < -3 and Star.getAbso() >= -6):
            return 'Bright Giants'
        elif(Star.getAbso() < -6 and Star.getAbso() >= -7):
            return 'Supergiants'
        elif(Star.getAbso() < -7):
            return 'Hypergiants'

    #Spectral Type F Categorization:
    elif(Star.getSpectral() == 'F'):
        if(Star.getAbso() >= 13 and Star.getAbso() <= 15):
            return 'White Dwarfs'
        elif(Star.getAbso() < 5 and Star.getAbso() >= 2 ):
            return 'Main Sequence'
        elif(Star.getAbso() < 2 and Star.getAbso() >= 1 ):
            return 'Subgiant'
        elif(Star.getAbso() < 1 and Star.getAbso() >= -1):
            return 'Giants'
        elif(Star.getAbso() < -1 and Star.getAbso() >= -4):
            return 'Bright Giants'
        elif(Star.getAbso() < -4 and Star.getAbso() >= -6):
            return 'Supergiants'
        elif(Star.getAbso() < -6):
            return 'Hypergiants'
    
    #Spectral Type G Categorization:
    elif(Star.getSpectral() == 'G'):
        if(Star.getAbso() >= 14 and Star.getAbso() <= 16):
            return 'White Dwarfs'
        elif(Star.getAbso() < 8 and Star.getAbso() >= 4 ):
            return 'Main Sequence'
        elif(Star.getAbso() < 4 and Star.getAbso() >= 2 ):
            return 'Subgiant'
        elif(Star.getAbso() < 2 and Star.getAbso() >= -1):
            return 'Giants'
        elif(Star.getAbso() < -1 and Star.getAbso() >= -3.5):
            return 'Bright Giants'
        elif(Star.getAbso() < -3.5 and Star.getAbso() >= -6):
            return 'Supergiants'
        elif(Star.getAbso() < -6):
            return 'Hypergiants'

    #Spectral Type K Categorization:
    elif(Star.getSpectral() == 'K'):
        if(Star.getAbso() >= 14 and Star.getAbso() <= 17):
            return 'White Dwarfs'
        elif(Star.getAbso() < 11 and Star.getAbso() >= 4 ):
            return 'Main Sequence'
        elif(Star.getAbso() < 4 and Star.getAbso() >= 2 ):
            return 'Subgiant'
        elif(Star.getAbso() < 2 and Star.getAbso() >= -1):
            return 'Giants'
        elif(Star.getAbso() < -1 and Star.getAbso() >= -3.5):
            return 'Bright Giants'
        elif(Star.getAbso() < -3.5 and Star.getAbso() >= -6):
            return 'Supergiants'
        elif(Star.getAbso() < -6):
            return 'Hypergiants'

    #Spectral Type M Categorization:
    elif(Star.getSpectral() == 'M'):
        if(Star.getAbso() <= 19 and Star.getAbso() >= 5 ):
            return 'Main Sequence'
        elif(Star.getAbso() < 2 and Star.getAbso() >= -2):
            return 'Giants'
        elif(Star.getAbso() < -2 and Star.getAbso() >= -3.5):
            return 'Bright Giants'
        elif(Star.getAbso() < -3.5 and Star.getAbso() >= -6):
            return 'Supergiants'
        elif(Star.getAbso() < -6):
            return 'Hypergiants'

    #Spectral Type L & T:
    elif((Star.getSpectral() == 'L' or Star.getSpectral() == 'T') and Star.getAbso() >= 10):
        if(Star.getMass() < 0.075):
            return 'Brown Dwarf'
        elif(Star.getMass() < 0.50):
            return 'Red Dwarf'
    
    #Otherwise, the star either hasn't been found in nature or is dead
    else:
        return 'Black Dwarf'

#=============================================================================#
# Simulation
#=============================================================================#

#Constants
G = 6.67408e-11 #Gravitational Constant
Msolar = 1.99e30 #Solar Mass in kg
Rsolar = 6.957e8 #Solar Radius, in m
Lsolar = 3.842e26 #Solar Luminosity in Watts
tSun = 4.6e9 #Time of sun
denSun = 1.622e5 #Central Density of Sun
m = 0.84e-27 #Half a proton mass
#Mean Molecular Weight (70% Hydrogen, 28% Helium, 2% Other) Ionized
mu = 0.62  
k = 1.38064852e-23 #Boltzman Constant
sigma = 5.697367e-8 #Stefan-Boltzman Constant
Q = 6.0e14 #Rate Energy that is released in J/kg
psi = 15/2
energyFromReaction = 4.32e-12
secondInYear = 3.154e7
massPerReaction = 6.692e-27

#=============================================================================#
# Random Generation
#=============================================================================#

#phi(M) = 0.060(M**-2.35) Salpeter Function
#Integral from 0.1 to 120 is 0.994918
norm = 1./(0.994918)

#Generation of randomized stars based on the distribution of stars in the
#our observable universe.
randMass = np.random.uniform(size=1)
randMass = -np.log(1-randMass/norm)
randMass = randMass*Msolar #Making it in Kg

#Modeling after the Sun
randMass = Msolar
density_c = denSun

#=============================================================================#
# Solving Lane-Emden Equation
#=============================================================================#

#From n = 0 to 4 by increments of 1, since 5 goes to infinity
laneSolutions = False #Set to false to do n=1.5

if(laneSolutions):
    nArray = [0.,1.,2.,3.,4.,3.25]
else:
    nArray = [3.25]

for n in nArray:

    #Boundary Conditions/Initial Values
    theta = 1. #Dimensionless Scaling Length
    dthetadxi = 0.
    
    #Setup
    xi = 0.0 #Dimensionless Radius
    dxi = 0.00001 #Time Step, lower the more accurate it is
    
    #Arrays
    thetaArray = []
    thetaArray.append(theta)
    dThetaArray = []
    dThetaArray.append(dthetadxi)
    xiArray = []
    xiArray.append(xi)
    
    #Loop until Scaling Length goes below time-step. (Roughly right before it
    # becomes negative)
    while theta > dxi:
        if(xi == 0):
            dthetadxi -= (theta**n * dxi)
        else:
            dthetadxi -= ( 2 * dthetadxi/xi + theta**n) * dxi
        theta += dthetadxi * dxi
        xi += dxi
        
        thetaArray.append(theta)
        dThetaArray.append(dthetadxi)
        xiArray.append(xi)
        
        
    #Results
    print('\n--------------------','\nxi_1:',xi)
    print('dTheta/dXi_1:',dthetadxi)
    
    xi_1 = xi
    dthetadxi_1 = dthetadxi
    
    #Plot
    plt.plot(xiArray,thetaArray,label='N = %s' % n)
    plt.xlabel('Dimensionless Length')
    plt.ylabel('Dimensionless Radius')

plt.title('Lane-Emden Solution')
plt.legend(loc='best')
plt.grid()
plt.show()

#=============================================================================#
# Finding K & Density from K (For iterations)
#=============================================================================#

def kConstant(mass,density):
    k = (((2) * (2*np.pi)**(1/3) * G * mass**(2/3) * density**((1/3)*(1-(3/n))))\
        /   (dthetadxi_1**(2/3) * (n**3 + 3*n**2 + 3*n + 1)**(1/3) * xi_1**(4/3)))
    return k
    
K = kConstant(randMass,density_c)

def densityFromK(mass):
    return ((-((((dthetadxi_1) * K**(3/2) * xi_1**2 * np.sqrt((n/G) + (1/G)))/(4 \
             * np.sqrt(np.pi) * G))+(((dthetadxi_1) * K**(3/2) * n * xi_1**2 * np.sqrt((n/G) + (1/G)))/(4 \
             * np.sqrt(np.pi) * G)))/mass)**((2*n)/(n-3))).real

print('K:',K)


#=============================================================================#
# Solving Initial Density & Radius
#=============================================================================#

avg_density = (-3/xi_1) * (dthetadxi_1) * (density_c)
print('Avg Density:',avg_density)

densityProp = density_c/avg_density
print('Proportion between Central Density & Avg. Density:', densityProp)

#In Solar Radius
def radius(density):
    return (((n+1)/(4*np.pi*G))**0.5 * K**(0.5) * density**((1-n)/(2*n)) * xi_1).real
             
starRadius = radius(density_c)
             
r_n2 = np.sqrt(starRadius/xi_1)
#pressure_c = 4 * np.pi * density_c * G * r_n2
def pressure(density):
    return K * density**(1+(1/n))

alpha = (((n+1)/(4*np.pi*G)) * K * density_c**(1/(n-1)))**0.5

def radius(xi):
    return xi * alpha


print('Mass:', Msolar)
print('Radius:',abs(starRadius))
print('Radius Percent %:',(abs(starRadius - Rsolar)/Rsolar) * 100)

#=============================================================================#
# Getting the remainder of the physical properties
#=============================================================================#

effRatio = 2722 #Ratio between Central Temperature and Effective Temp

#The Effective Temperature of the Sun is approximately 2722 times less than the
#Central Temperature
def temp(density):
    return (((pressure(density) * mu*m * (K**n) * (k / (mu*m))**(-n))/k)**(1/(n+1))/effRatio).real

def Lum(temp,radius):
    return abs((4 * np.pi * radius**2 * sigma * temp**4).real)


initialTemp = temp(density_c)
initialLum = Lum(initialTemp,starRadius)
print('Temperature:', initialTemp)
print('Luminosity:', initialLum)

#=============================================================================#
# Time Dependent Variable Luminosity
#=============================================================================#

#Derived Lumonistiy function with respect to time
def L(t,mass):
    l = (initialLum) * (1 - (5/4)*(psi + 1)*((mu * initialLum)/(mass * Q))*t)\
    **((-psi)/(psi+1))
    return abs(l)


def massLoss(lum,time):
    reactPerSec = lum/energyFromReaction
    #Time convert from secons to years
    return reactPerSec * massPerReaction * (time * secondInYear)

#=============================================================================#
# Creation of First Star and all it's physical properties
#=============================================================================#

starZero = Star(randMass,initialLum,starRadius,initialTemp)
starArray = []
starArray.append(starZero)

#=============================================================================#
# Simulation
#=============================================================================#

N = 1000 #Number of Time Slices
time_space = np.linspace(1,1e9,N) #Time from 1 Year to 10 Billion Years
                    
for t in time_space:
    
    #Mass Change from temperatrure difference
    lum = L(t,randMass)
    mass = starArray[len(starArray)-1].getMass() - massLoss(lum,t)
    centralDensity = densityFromK(mass)
    radiusStar = radius(centralDensity)
    centralPressure = pressure(centralDensity)
    temperature = temp(centralDensity)
    
    newStar = Star(mass,lum,radiusStar,temperature)
    starArray.append(newStar)

#=============================================================================#
# Plots
#=============================================================================#

temperatures = []
luminosities = []
radiuses = []
masses = []
for x in range(len(starArray)-1):
    temperatures.append(starArray[x].getTemp())
    masses.append(starArray[x].getMass())
    luminosities.append(starArray[x].getLum())
    radiuses.append(starArray[x].getRadius())

#Temperature    
plt.figure()
plt.plot(time_space,temperatures)
plt.title('Time vs. Effective Temperature')
plt.xlabel('Time (Years)')
plt.ylabel('Effective Temperature (K)')
plt.grid()

#Luminosity
plt.figure()
plt.plot(time_space,luminosities)
plt.title('Time vs. Luminosity')
plt.xlabel('Time (Years)')
plt.ylabel('Luminosity (J/s)')
plt.grid()

#Radius
plt.figure()
plt.plot(time_space,radiuses)
plt.title('Time vs. Radius')
plt.xlabel('Time (Years)')
plt.ylabel('Radius (m)')
plt.grid()

#Mass
plt.figure()
plt.plot(time_space,masses)
plt.title('Time vs. Mass')
plt.xlabel('Time (Years)')
plt.ylabel('Mass (kg)')
plt.grid()

plt.show()



