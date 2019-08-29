# -*- coding: utf-8 -*-
"""
Created on Mon Jul 22 15:08:37 2019
@author: bllrd

purpose: Stores variables that remain constant for a set of data or a run of the code.

University of Michigan
"""
import numpy as np
### difference between slices and bin width?

# what the data will go through
PSDRANGE = 99
CHANNELS = 48

#channels that need to be excluded
EXCLUDED_CHANNELS = [0, 1, 16, 17, 32, 33]

#ROWS = 1e7
CHUNK_SIZE = 5e5

# slice demensions
MAX_E = 6 #keep at 5.2 or lower to run through more than the inital graphs
MIN_E = .5 #.5
BIN_WIDTH = 1
SLICENUMBER = int((MAX_E - MIN_E) / BIN_WIDTH)
SLICE_AXIS = np.linspace(MIN_E, MAX_E - BIN_WIDTH, SLICENUMBER)
STOP = SLICENUMBER - 1

MODE = 2 #needs to be at one to assign type
#mode key
    # CENTER_DISCRIMINATION = 1
    # INTERSECTION_DISCRIMINATION = 2
    #COEFFICENTS = 3

#COEF_FILE = "psdcoeff.i"
#KEY_WORD = '#channel_nr'
SAVE_PATH = '/Users/bllrd/.spyder-py3/Research/PSD/Figures/'

#psd axis variables
MIN_PSD = 0
MAX_PSD = .5
NUM_PSD_BINS = 100
PSD_BIN_WIDTH = ((MAX_PSD - MIN_PSD) / NUM_PSD_BINS)
GRAPH_AXIS = np.linspace(MIN_PSD, MAX_PSD, NUM_PSD_BINS)

#set prediction for the sigma of the gaussian curves
SIGMA_GUESS = [0.05, 0.06]
#set prediction for the centers of the gaussian curves
CENTER_GUESS = [.15, .29, .175, .27]



