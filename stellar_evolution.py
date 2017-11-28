# -*- coding: utf-8 -*-
"""
Created on Mon Nov  6 02:56:18 2017

@author: Steven Li
"""

import numpy as np
import matplotlib.pyplot as plt
import main_sequence

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
# Random Generation
#=============================================================================#

randMass = np.random.randint(0.01,10) 
randRadius = np.random.randint(0.01,200)
randLumonsity = np.random.randint(0.01,50000)
randTemp = np.random.randint(0.01,32000)

randomStar = Star(randMass,randLumonsity,randRadius,randTemp)
print(randomStar)

#=============================================================================#
# Simulation
#=============================================================================#

#phi(M) = 0.060(M**-2.35) Salpeter Function
#Integral from 0.1 to 120 is 0.994918

norm = 1./(0.994918)

randMass = np.random.uniform(size=1)
randMass = -np.log(1-randMass/norm)

#Constants
G = 6.67408e-11 #Gravitational Constant
Msolar = 1.99e33 #Solar Mass
Rsolar = 6957e5 #Solar Radius
m = 0.84e-27 
mu = 0.5  #Completely Hydrogen, Mean Molecular Weight

#=============================================================================#
# Solving Lane-Emden Equation
#=============================================================================#

#From n = 0 to 4 by increments of 1, since 5 goes to infinity
laneSolutions = False #Set to false to do n=1.5

if(laneSolutions):
    nArray = [0.,1.,2.,3.,4.]
else:
    nArray = [1.5]

for n in nArray:

    #Boundary Conditions
    theta = 1. #Dimensionless Scaling Length
    dthetadxi = 0. 
    density_c = 1
    
    #Setup
    xi = 0.0 #Dimensionless Radius
    dxi = 0.000001 #Time Step, lower the more accurate it is
    
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
plt.show()

#=============================================================================#
# Finding K
#=============================================================================#

K = abs(((-2)**(2/3) * np.pi**(1/3) * G * randMass**(2/3) * density_c**(1/3)*(1-(3/n)))\
        /   ((-xi_1**2 * dthetadxi_1)**(2/3) * (n**3 + 3*n**2 + 3*n + 1)**(1/3)))

#K = ((4*np.pi)**(1/n) / (n+1)) * -(xi_1**2 * dthetadxi_1)**((1-n)/n) * xi_1**((n-3)/n)\
#    * G * randMass**((n-1)/n) * starRadius**((3-n)/n)

#K = - ((G(4*np.pi)**(1/n)) * (xi_1**((n+1)/(1-n))) * randMass**((n-1)/n) \
#      * starRadius**((3/n)-1) * (dthetadxi_1 * (xi_1**((n+1)/(1-n))))**(1/n)) \
#       / (dthetadxi_1 * (n+1))

print('K:',K)

#=============================================================================#
# Solving Avg Density
#=============================================================================#

avg_density = (-3/xi_1) * (dthetadxi_1) * (density_c)
print(avg_density)

alpha = (((n+1)/(4*np.pi*G)) * K * density_c**(1/(n-1)))**0.5

def radius(xi):
    return xi * alpha

starRadius = ((n+1)/(4*np.pi*G))**0.5 * K**(0.5) * density_c**((1-n)/(2*n)) * xi_1
             
r_n2 = (starRadius/xi_1)**2
pressure_c = 4 * np.pi * density_c * G * r_n2

print('Mass:',randMass)
print('Radius:',abs(starRadius))

#=============================================================================#
# Getting the remainder of the physical properties
#=============================================================================#



