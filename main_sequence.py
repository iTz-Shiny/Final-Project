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


#------------------------------------------------------#