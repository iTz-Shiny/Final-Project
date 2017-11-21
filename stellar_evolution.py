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

randMass = np.random.randint(0.01,100) 
randRadius = np.random.randint(0.01,200)
randLumonsity = np.random.randint(0.01,50000)
randTemp = np.random.randint(0.01,32000)

randomStar = Star(randMass,randLumonsity,randRadius,randTemp)
print(randomStar)

#=============================================================================#
# Simulation
#=============================================================================#

#Setup
N = 50 #Number of Time Slices

lifeTime = main_sequence.lifetime(randMass)
time_space = np.linspace(lifeTime,0,N)
star_space = []

star_space.append(randomStar)

#Equations
def dT(Star):
    return Star.get


#Loop

for n in range(1,N-2):
    
    nthTime = time_space[n]
    
    
    
    
    
    
    
    
