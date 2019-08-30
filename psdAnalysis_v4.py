# -*- coding: utf-8 -*-
"""
Created on Mon Jul 22 14:59:23 2019
@author: bllrd

purpose: Connects to all of the files. Acesses and stores the data. Runs the 
    definitions in other files.
    
functions that can be run:
    rawGraph: graphs the data
    plotByDensity: (scatterplot colored by density)
    notSliced: (plots unsliced data with two gaussian curves)
    
    sliceByIntegralWithGaussian: (histograms data in slices (by integral bins) with two gaussian curves)
    discrimLine: (uses the data from sbiwg and finds a discrimination line for each slice)
    findError: (finds the integral under each gaussian from the discrimination line)
    classify:(types the data using the discrimination line)

University of Michigan
"""
import pandas as pd
import psdConstants_v4 as psdC
import matplotlib.pyplot as plt

import densityPlots_v4 as denP

#switches for the different types of graphs
rawGraph = False
density = True

#Saves data under "data" so it can be acessed 
path = '/Users/bllrd/.spyder-py3/Research/PSD/Data/'
file = 'psdfile'
number = 2
data =  pd.read_csv(path + file + str(number),
    header = None, delim_whitespace = True,
    nrows = psdC.ROWS, names = ['History',
                          'Type',
                          'PSD',
                          'Integral',
                          'Height'])
    
#shortcuts for grabbing data 
bothPSD = data.PSD
bothIntegral = data.Integral
neutronPSD = data[data.Type == 1].PSD
neutronIntegral = data[data.Type == 1].Integral
photonPSD = data[data.Type == 2].PSD
photonIntegral = data[data.Type == 2].Integral
neutronHeight = data[data.Type == 1].Height
photonHeight = data[data.Type == 2].Height

#graphing functions that have to be turned on
if rawGraph:
    #prints plain psd graph
    plt.scatter(photonPSD, photonIntegral, psdC.XAXIS, color = 'r', alpha = 0.5)
    plt.scatter(neutronPSD, neutronIntegral, psdC.XAXIS, color = 'b', alpha = 0.5)
if density:
    #plota psd vs integral values by density 
    denP.plotByDensity(data, psdC.SAVE_PATH, psdC.SLICE_AXIS)

