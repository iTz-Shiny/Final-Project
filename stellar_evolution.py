# -*- coding: utf-8 -*-
"""
Created on Mon Nov  6 02:56:18 2017

@author: Steven Li
"""

#11 Types of Stars:
    '''
    Hypergiant
    Supergiant
    Bright giants
    Giants
    Subgiants
    Main Sequence Dwarfs
    Sub-dwarfs
    Red-dwarfs
    Brown-dwarfs
    White-dwarfs  
    Black-dwarfs (Dead Star)
    '''

class Star(mass, lumonsity, radius, temperature):
    
    def __init__(self, mass, lumonsity, radius, temperature):
        self.mass = mass
        self.lumonsity = lumonsity
        self.radius = radius
        self.temperature = temperature
    

#Based on Mass, Lumonsity, Radius, and Temperature. Attempt to identify
#what category the star fits into and determine it's lifetime(if not already done).
#Then stimulate the evolution of the star. Assuming that the star is singular and
#receives no outside influence such as gathering mass from other stars during it's
#collapse

#Possible outcomes of stellar evolution evolution: Supernova into Neutron Star/Black Hole
#or into a black-dwarf eventually(unless acted upon from another star)