# -*- coding: utf-8 -*-
"""
Created on Wed Aug 14 16:11:05 2019
@author: bllrd

purpose: Find the missclassification of a larger amount of data based of gaussian curves
        and a discrimination line.

University of Michigan
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import psdConstants_v4 as psdC

import AssignDE_v4 as adE
import createGaussian_v4 as crG
import discrimLine_v4 as fdL
import FindError_v4 as fdE
#import coeffFinder as coF

path = '/Users/bllrd/.spyder-py3/Research/PSD/Data/largePSDdata/'
file = 'psdfile'
minFile = 3
maxFile = 18

font = {'family' : 'normal', #(Herman Schaaf)
        'weight' : 'normal',
        'size'   : 13} #fonts library DNNG


#holds all of the PSDs for the data so they can be accessed later
psdArray = [
            [
             []
              for i in range(0, psdC.SLICENUMBER + 2)]
                for i in range(0, psdC.CHANNELS)]



#data gathering, reads from files in chunks
for number in range(minFile, maxFile):
    for portion in pd.read_csv(path + file + str(number),
                               header = None, delim_whitespace = True,
                               chunksize = psdC.CHUNK_SIZE,
                               names = ['History',
                                        'Type',
                                        'PSD',
                                        'Integral',
                                        'Height',
                                        'Channel']):
        # stores needed data in lists
        channels = np.array(portion.Channel)
        energies = np.array(portion.Integral)
        psd = np.array(portion.PSD)
        # puts the data into the array based on channel and energy (see assignDE.py)
        for i in range(0, len(channels)):
            psdArray[channels[i]][adE.assignEnergy(energies[i], psdC.BIN_WIDTH,
                                                                psdC.MIN_E,
                                                                psdC.MAX_E,
                                                                psdC.SLICENUMBER)] += [psd[i]]


print('have data')

# arrays for error values to be put into based on channel
npErrorArray = [[]for i in range(0, psdC.CHANNELS)]
pnErrorArray = [[]for i in range(0, psdC.CHANNELS)]

# place for discrimline values to be put into based on channel
discrimLineArray = [[]for i in range(0, psdC.CHANNELS)]

# loops through channels
for thisChannel in range(0, psdC.CHANNELS):
    # checks that the channel is one that should be looked at
    if not (thisChannel in psdC.EXCLUDED_CHANNELS):
        # loops through energies
        for energies in range(1, len(psdArray[thisChannel]) - 1):

            # saves a slice of data for the definitions to use
            psdSlice = psdArray[thisChannel][energies]
    
            # fits two seperate gaussian curves with the slice of data, and saves
            #   their parameters (createGaussian.py)
            gaussListPhoton, gaussListNeutron, photonC, photonS, neutronC, neutronS, center = crG.fitSlice(psdSlice, psdC.CENTER_GUESS, psdC.PSD_BIN_WIDTH, psdC.SIGMA_GUESS, psdC.GRAPH_AXIS, thisChannel)
           
            # At this stage we have: two gaussian curves
            # finds the discrimination line (discrimLine2.py)
            discrimLine = fdL.findDiscrimLine(psdC.MODE, photonC, neutronC, gaussListPhoton, gaussListNeutron, center)
            
            # at this stage we have: a discrimination line and gaussian curve data
            # finds the shift needed to make the error equal for both particle types
            # finds the error for each particle
            npError, pnError, discrimLine2 = fdE.neutronPhotonError(discrimLine, photonC, neutronC, photonS, neutronS)
            npErrorArray[thisChannel] += [npError]
            pnErrorArray[thisChannel] += [pnError]
            #discrimLineArray[thisChannel] += [discrimLine2]
            
            #saves graphs of the data with gaussians and a discrimination line 
            # by detector and slice (creategaussian.py)
            crG.plotSBI(psdSlice, gaussListPhoton, gaussListNeutron, photonC, photonS, neutronC, neutronS, center, discrimLine2, psdC.GRAPH_AXIS, thisChannel, energies, psdC.SAVE_PATH)



# error graph by energies
energyNPError = []
energyPNError = []


### maybe use "energies in detectorAxis:"
for energies in range(0, psdC.SLICENUMBER):
    #place to put a lists of errors into
    avgnpError = []
    avgpnError = []

    #adds only the error of certain particles into the arrays
    for thisChannel in range(2, len(npErrorArray)):
        if not thisChannel in psdC.EXCLUDED_CHANNELS:
            avgnpError += [npErrorArray[thisChannel][energies]]
            avgpnError += [pnErrorArray[thisChannel][energies]]

    #takes the average of each list ingoring null areas
    npCleaned = [x for x in avgnpError if str(x) != 'nan']
    pnCleaned = [x for x in avgpnError if str(x) != 'nan']

    #adds the average into a list of averages
    energyNPError += [np.average(npCleaned)]
    energyPNError += [np.average(pnCleaned)]



#plots a graph of the slices by average errors for each slice
fig = plt.figure()
plt.plot(psdC.SLICE_AXIS, energyPNError, 'or', label = 'P to N')
plt.plot(psdC.SLICE_AXIS, energyNPError, 'ob', label = 'N to P')
plt.xlabel('Energy (Integral MeVee)')
plt.ylabel('Misclassification Rate')
plt.title('Average Misscalassification Rates per Slice')
plt.legend()
plt.show(fig)
fig.savefig(psdC.SAVE_PATH + 'Error.png')
plt.close(fig)


##arrays to put in the data that needs to be saved
#exportNP = [[] for i in range(1, psdC.SLICENUMBER-1)]
#exportPN = [[] for i in range(1, psdC.SLICENUMBER-1)]
#
##adds data into the arrays
#for slices in range(1, psdC.SLICENUMBER - 1):
#    exportPN[slices] += [slices, energyPNError[slices]]
#    exportNP[slices] += [slices, energyNPError[slices]]

 # try the following instead
np.savetxt( psdC.SAVE_PATH + 'missclassNG.csv', np.array(energyNPError), delimiter = ','  )
np.savetxt( psdC.SAVE_PATH + 'missclassGN.csv', np.array(energyPNError), delimiter = ','  )
np.savetxt( psdC.SAVE_PATH + 'energySlices.csv', np.array(psdC.SLICE_AXIS), delimiter = ',')
 # and you will have two lists with the misclassification, and one which tells you which energy they correspond to

##saves the data into a file using csv format
#np.savetxt( psdC.SAVE_PATH + 'missclassificationNG.csv', np.array(exportNP), delimiter = ','  )
#np.savetxt( psdC.SAVE_PATH + 'missclassificationGN.csv', np.array(exportPN), delimiter = ','  )
