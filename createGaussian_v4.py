# -*- coding: utf-8 -*-
"""
Created on Fri Aug 16 09:41:48 2019

@author: bllrd
"""
import numpy as np
import matplotlib.pyplot as plt
import scipy.optimize as sciPy



def fitSlice(psdSlice, centers, psdBinWidth, sigmaGuess, xAxis, channel):

    [psdCounts, psdEdge] = np.histogram(psdSlice, xAxis)
    center = (psdEdge[:-1] + psdEdge[1:]) /2
    
    if channel >= 40:
        p = 2
        n = 3
    else:
        p = 0
        n = 1
 #Photon curve
    centerPhoton = int(centers[p]/psdBinWidth)
    amplitudePhoton = max(psdCounts)
    widthPhoton = int(sigmaGuess[0] / psdBinWidth)
    domainPhotons =  center[int(centerPhoton - widthPhoton) : int(centerPhoton + widthPhoton)]
    rangyPhotons = psdCounts[int(centerPhoton - widthPhoton) : int(centerPhoton + widthPhoton)]
    p0Photon = [amplitudePhoton, center[centerPhoton], sigmaGuess[0]]
    poptPhotons, variances = sciPy.curve_fit(gauss, domainPhotons, rangyPhotons, p0 = p0Photon)
    gaussListPhoton = []
    for x in center:
        gaussListPhoton += [gauss(x, poptPhotons[0], poptPhotons[1], poptPhotons[2])]

# Neutron curve
    centerNeutron = int(centers[n] / psdBinWidth)
    amplitudeNeutron = psdCounts[centerNeutron]
    widthNeutron = int(sigmaGuess[1] / psdBinWidth)
    domainNeutrons =  center[int(centerNeutron - widthNeutron) : int(centerNeutron + widthNeutron)]
    rangyNeutrons = psdCounts[int(centerNeutron - widthNeutron) : int(centerNeutron + widthNeutron)]
    p0Neutron = [amplitudeNeutron, center[centerNeutron], sigmaGuess[1]]
    poptNeutrons, variances = sciPy.curve_fit(gauss, domainNeutrons, rangyNeutrons, p0 = p0Neutron)
    gaussListNeutron = []
    for x in center:
        gaussListNeutron += [gauss(x, poptNeutrons[0], poptNeutrons[1], poptNeutrons[2])]

    photonC = poptPhotons[1]
    photonS = poptPhotons[2]
    neutronC = poptNeutrons[1]
    neutronS = poptNeutrons[2]
    
    # plot and save to data
    # ig.savefig(PATH + path.PATH_DELAYS + '/' + path.PATH_CURVES + '/' + str(FOLDER) + '/' + str(channelOffset) + path.DELAY_TOF_CHANNEL)
    # plt.close(fig)


    return gaussListPhoton, gaussListNeutron, photonC, photonS, neutronC, neutronS, center


#Gives you the y-value of a gaussian for any given x
def gauss(x, *p): ### importantDistributions
    A, mu, sigma = p
    return A*np.exp(-(x-mu)**2/(2.*sigma**2))


def plotSBI(psdSlice, photonData, neutronData, photonC, photonS, neutronC, neutronS, center, discrimLine, xAxis, thisChannel, energies, savepath):
        
    #saves the location of the data to label the graphs
    detector = thisChannel
    energy = energies
    
    #plots the histogram with the two gaussian curves and the discrimination line
    fig = plt.figure()
    plt.hist(psdSlice, xAxis, alpha = .5, color = 'y')
    plt.plot(center, photonData, color = 'r', label = 'Photon')
    plt.plot(center, neutronData, color = 'b', label = 'Neutron')
    plt.axvline(x = discrimLine, c = 'k')
    plt.xlabel('PSD')
    plt.ylabel('Counts of Particles')
    plt.title('Sliced PSD by Integral  ' + str(detector) + '_' + str(energy))
    plt.legend()
    fig.savefig(savepath + 'slice_' + str(detector) + '_' + str(energy) + '.png')
    #plt.show()
    plt.close()
            
    return 