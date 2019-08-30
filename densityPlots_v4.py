# -*- coding: utf-8 -*-
"""
Created on Tue Jul 16 14:03:11 2019
@author: bllrd

purpose: Stores a definition that can plot a scatterplot of any two datasets 
    that is colored by density. 
    
University of Michigan
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import gaussian_kde


#import UniformToNormal as utn
#import scipy.optimize as sciPy

#makes a plot of the psd by integral data by density
def plotByDensity(data, savepath, xaxis):
    # gathers data
    x = data[data.Integral >= 0].PSD
    y = data[data.Integral >= 0].Integral 
    
    #plots data
    fig = plt.figure()
    plt.hist2d(x, y, (100, 100), ((0, .45), (0, 20)), cmap=plt.cm.jet)
    plt.colorbar()
    plt.xlabel('PSD')
    plt.ylabel('Integral')
    fig.savefig(savepath + 'densityPlot.png')
    plt.show()
    return


