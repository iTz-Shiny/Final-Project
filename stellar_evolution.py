# -*- coding: utf-8 -*-
"""
Created on Mon Nov  6 02:56:18 2017

@author: Steven Li
"""

import numpy as np
import matplotlib.pyplot as plt

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
    Black - dwarfs ( Dead Star)
'''
#Possibly will have multiple classes of stars and change them to specific classes
#when
#specific parameters have been met to keep track of current star type throughout
#calculations.
class Star ( mass , luminosity , radius , temperature ):
    
    def __init__ ( self , mass , luminosity , radius , temperature ):
        self.mass = mass
        self.lum = luminosity
        self.radius = radius
        self.temp = temperature
        self.spectral = spectral()
        self.absoMag = absoMag(lum)
        self.starType = catergorize()
        
    def setStar():
        self.type = categorize()
        
    def setSpectral():
        self.spectral = spectral()
        
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

def spectral():
    '''
    Categorize star into it's respective stellar classification    
    '''
    if(temp >= 30000 and mass >= 16 and radius >= 6.6 and lum >= 30,000):
        return 'O'
    elif(temp >= 10000 and mass >= 2.1 and radius >= 1.8 and lum >= 25):
        return 'B'
    elif(temp >= 7500 and mass >= 1.4 and radius >= 1.4 and lum >= 5):
        return 'A'
    elif(temp >= 6000 and mass >= 1.04 and radius >= 1.15 and lum >= 1.5):
        return 'F'
    elif(temp >= 5200 and mass >= 0.8 and radius >= 0.96 and lum >= 0.6):
        return 'B'
    elif(temp >= 3700 and mass >= 0.45 and radius >= 0.7 and lum >= 0.08):
        return 'K'
    elif(temp >= 2400 and mass >= 0.08 and radius <= 0.7 and lum <= 0.08):
        return 'M'
    elif(temp >= 1300 and temp <= 2000 and mass >= 0.06 and mass <= 0.08):
        return 'L'
    elif(temp >= 550 and temp <= 1300 and mass <= 0.06):
        return 'T'
    
def absoMag(lum):
    solarLum = 3.828e-26
    return -2.5*np.log10(lum*solarLum) + 71.197425
    
def categorize():
    
    #Spectral Type O Categorization
    if(self.spectralClass == 'O'):
        if(absoMag >= 8 and absoMag <= 11):
            self.starType = 'White Dwarfs'
        elif(absoMag <= 0 and absoMag >= -4 ):
            self.starType = 'Main Sequence'
        elif(absoMag <= -4 and absoMag >= -5):
            self.starType = 'Giants'
        elif(absoMag <= -5 and absoMag >= -6):
            self.starType = 'Bright Giants'
        elif(absoMag <= -6 and absoMag >= -7):
            self.starType = 'Supergiants'
        elif(absoMag <= -7):
            self.starType = 'Hypergiants'
       
    #Spectral Type B Categorization:
    if(self.spectralClass == 'B'):
        if(absoMag >= 9 and absoMag <= 13):
            self.starType = 'White Dwarfs'
        elif(absoMag <= 2 and absoMag >= -3 ):
            self.starType = 'Main Sequence'
        elif(absoMag <= -3 and absoMag >= -4):
            self.starType = 'Giants'
        elif(absoMag <= -4 and absoMag >= -6):
            self.starType = 'Bright Giants'
        elif(absoMag <= -6 and absoMag >= -7):
            self.starType = 'Supergiants'
        elif(absoMag <= -7):
            self.starType = 'Hypergiants'
        
    #Spectral Type A Categorization:
    if(self.spectralClass == 'A'):
        if(absoMag >= 10 and absoMag <= 14):
            self.starType = 'White Dwarfs'
        elif(absoMag < 4 and absoMag >= 2):
            self.starType = 'Main Sequence'
        elif(absoMag < 2 and absoMag >= 0):
            self.starType = 'Subgiants'
        elif(absoMag < 0 and absoMag >= -3):
            self.starType = 'Giants'
        elif(absoMag < -3 and absoMag >= -6):
            self.starType = 'Bright Giants'
        elif(absoMag < -6 and absoMag >= -7):
            self.starType = 'Supergiants'
        elif(absoMag < -7):
            self.starType = 'Hypergiants'

    #Spectral Type F Categorization:
    if(self.spectralClass == 'F'):
        if(absoMag >= 13 and absoMag <= 15):
            self.starType = 'White Dwarfs'
        elif(absoMag < 5 and absoMag >= 2 ):
            self.starType = 'Main Sequence'
        elif(absoMag < 2 and absoMag >= 1 ):
            self.starType = 'Subgiant'
        elif(absoMag < 1 and absoMag >= -1):
            self.starType = 'Giants'
        elif(absoMag < -1 and absoMag >= -4):
            self.starType = 'Bright Giants'
        elif(absoMag < -4 and absoMag >= -6):
            self.starType = 'Supergiants'
        elif(absoMag < -6):
            self.starType = 'Hypergiants'
    
    #Spectral Type G Categorization:
    if(self.spectralClass == 'G'):
        if(absoMag >= 14 and absoMag <= 16):
            self.starType = 'White Dwarfs'
        elif(absoMag < 8 and absoMag >= 4 ):
            self.starType = 'Main Sequence'
        elif(absoMag < 4 and absoMag >= 2 ):
            self.starType = 'Subgiant'
        elif(absoMag < 2 and absoMag >= -1):
            self.starType = 'Giants'
        elif(absoMag < -1 and absoMag >= -3.5):
            self.starType = 'Bright Giants'
        elif(absoMag < -3.5 and absoMag >= -6):
            self.starType = 'Supergiants'
        elif(absoMag < -6):
            self.starType = 'Hypergiants'

    #Spectral Type K Categorization:
    if(self.spectralClass == 'K'):
        if(absoMag >= 14 and absoMag <= 17):
            self.starType = 'White Dwarfs'
        elif(absoMag < 11 and absoMag >= 4 ):
            self.starType = 'Main Sequence'
        elif(absoMag < 4 and absoMag >= 2 ):
            self.starType = 'Subgiant'
        elif(absoMag < 2 and absoMag >= -1):
            self.starType = 'Giants'
        elif(absoMag < -1 and absoMag >= -3.5):
            self.starType = 'Bright Giants'
        elif(absoMag < -3.5 and absoMag >= -6):
            self.starType = 'Supergiants'
        elif(absoMag < -6):
            self.starType = 'Hypergiants'

    #Spectral Type M Categorization:
    if(self.spectralClass == 'M'):
        if(absoMag <= 19 and absoMag >= 5 ):
            self.starType = 'Main Sequence'
        elif(absoMag < 2 and absoMag >= -2):
            self.starType = 'Giants'
        elif(absoMag < -2 and absoMag >= -3.5):
            self.starType = 'Bright Giants'
        elif(absoMag < -3.5 and absoMag >= -6):
            self.starType = 'Supergiants'
        elif(absoMag < -6):
            self.starType = 'Hypergiants'

    #Spectral Type L & T:
    if(self.spectralClass == 'L' or self.spectralClass = 'T'):
        if(self.mass < 0.075):
            self.starType = 'Brown Dwarf'
        else:
            self.starType = 'Red Dwarf'
    
    
    
    
    
    
    
    
    
    
    
    
