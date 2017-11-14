# -*- coding: utf-8 -*-
"""
Created on Mon Nov  6 01:01:03 2017

@author: Steven Li
"""

#Main Sequence Stars
#Parameters relative to the sun except Temperature
'''Parameters:
    Radius: 0.16 - 15
    Mass: 0.10 - 60
    Luminosity: 3e-3 - 790000
    Temperature(K): 2900 - 44,500
'''

#Solar Unit Conversions
'''
    1 Solar Luminosity: 3.828e26 W
    1 Solar Mass: 1.99e30 kg
    1 Solar Radii: 695700 km
'''

#Mass-Luminosity Relation for mass < .43 Solar Mass
def lum(Mass):
    '''
    Returns the Lumonsity of a main sequence star
    based on it's mass. Depending on the mass, the star
    will exhibit different amount of Lumonsity. As the
    mass increases, the luminosity becomes increasingly
    equiavelent to the change in mass.
    '''
    if Mass < .43:
        return .23*(Mass)**2.3
    elif Mass < 2:
        return Mass**4
    elif Mass < 20:
        return 1.5 * Mass**3.5
    else:
        return 3200*Mass
    
#Lifetime of a Main Sequence Star in years
def lifetime(Mass):
    '''
    Returns the lifetime of a main sequence star based on it's relation
    to mass.
    '''
    return 100*Mass**-2.5

#------------------------------------------------------#
# Rate of Energy Spent
#------------------------------------------------------#

#Main Sequence Stars utilize Nuclear Fusion to generate it's energy
#Assuming that the majority of stars undergo Hydrogen Burning which is
#a nuclear reaction between Hydrogen and Helium. I will use Helium-4 nucleus
#as the main atom created from the fusion. The production of each helium-4 nucleus
#requires 4.3e-12 J of energy. Which if I use the lumonsity of a star divided
#by that value then that would be the number of Helium-4 required to be formed
#every second to maintain it's lumonsity. 4 Protons are used to create a Helium-4
#nucleus and the mass loss is 0.7% or 0.029amu. This is the rate of mass loss per Helium-4
#creation. Utilzing E=mc^2 with this data, and the mass of Hydrogen in the core
#where the reaction happens in main-sequence stars which is usually 10% of the mass of
#the star. You can find the total Energy possible for the star to produce

#In AMU measurements
proton = 1.008
helium4 = 4.003
massLoss = 0.029
amu = 1.7e-27

heliumE = (massLoss*amu)*(3e8)**2 #E=mc^2

def energyPerS(lum): #Rate of Energy Lost
    return (lum*3.828e26) / heliumE

def totalEnergy(ener): #Total Energy based on how mcuh Hydrogen remains
    return 0


