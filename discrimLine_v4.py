# -*- coding: utf-8 -*-
"""
Created on Wed Aug 14 12:16:44 2019
@author: bllrd

purpose: Definition that takes the data from slicedByIntegral and finds a
        discrimination line for each slice.

        mode 1: finds the midpoint in refrence to the two maxes
        mode 2: finds the intesection of the two gaussians
        mode 3: makes a line using constants [A, B, C]

University of Michigan
"""
import numpy as np

MIDPOINT_MODE = 1
INTERSECTION_MODE = 2

#finds Discrim line
def findDiscrimLine(mode, photonC, neutronC, photonData, neutronData, centers):
    discrimLine = []
    if mode == MIDPOINT_MODE: #center discrimination
        discrimLine = (photonC + neutronC) / 2
    elif mode == INTERSECTION_MODE: #intersection discrimination
        for index in range(0, len(neutronData) - 1):
            if photonData[index] - neutronData[index] >= 0 and photonData[index + 1] - neutronData[index + 1] <= 0:
                discrimLine = centers[index]
                #discrimLine = np.average(discrimLines)
    return discrimLine

#uses constants to create a quadratic line for all of the data 
#   then uses the quadratic to find a line for each slice
def findDiscrimLineWConstants(constants, energies, sliceN):
    discrimLine = []
    x = energies + (sliceN / 2)
    discrimLine += [(constants[0] * (x ** 2)) + (constants[1] * x) + constants[2]]
    return discrimLine

