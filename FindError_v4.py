# -*- coding: utf-8 -*-
"""
Created on Wed Jul 24 13:43:51 2019
@author: bllrd

purpose: Definition that finds the areas under two seperate gaussian
     curves at the same line that intersects both curves.
     (finds the misclassification rate of photons and neutrons)

University of Michigan
"""
#imports
from scipy.stats import norm

#finds the area under the gaussians from on the discrimination line using normalcdf
def neutronPhotonError(discrimLine, photonC, neutronC, photonS, neutronS):
    nError = 1
    pError = 0
    newDiscrimLine = discrimLine
    #finds the delta (findDelta)
    delta = findDelta(discrimLine, photonC, neutronC, photonS, neutronS)
    newDiscrimLine = delta
#
    #neutron to gamma error
    nError = norm(neutronC, neutronS).cdf(newDiscrimLine)

    #gamma to neutron error
    pError = 1 - norm(photonC, photonS).cdf(newDiscrimLine)

    return nError, pError, newDiscrimLine

#finds the shift needed to make the errors equal
def findDelta(discrimLine, photonC, neutronC, photonS, neutronS):
    num = (photonC * neutronS) + (neutronC * photonS)
    denom =  neutronS + photonS
    delta = (num / denom)
    return delta
