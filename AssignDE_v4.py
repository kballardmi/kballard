# -*- coding: utf-8 -*-
"""
Created on Thu Aug 15 12:01:02 2019

@author: bllrd
"""

# assigns a bin for each particle based on its Integral using the bin parameters
def assignEnergy(energy, binWidth, eMin, eMax, numSlices):
    # between the parameters, starts at bin 1, goes to the last bin
    if energy >= eMin and  energy < eMax:
        energySlot = int( (energy - eMin) / binWidth) + 1
    # lower than the low parameter, goes into bin 0
    elif energy <= eMin:
        energySlot = 0
    # higher than the high parameter, goes into the last bin
    elif energy >= eMax:
        energySlot = numSlices - 1
    return energySlot
