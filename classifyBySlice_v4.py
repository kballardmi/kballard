# -*- coding: utf-8 -*-
"""
Created on Mon Jul 22 15:08:37 2019
@author: bllrd

purpose: Definition that uses the discrimination lines to determine if a particle is a neutron
        or a photon. Only slices positive data.

University of Michigan
"""

import numpy as np
import matplotlib.pyplot as plt

def findType(minEnergy, maxEnergy, sliceNumber, data, discrimLine, xAxis, binWidth, slices):
    typeSlice = []
    integrals = data.Integral
    psds = data.PSD
#types
    for particle in range(0, len(data)):
        integral = integrals[particle]
        psd = psds[particle]
        sliceIndex = int(integral / binWidth)
        if integral >= minEnergy and integral <= maxEnergy and sliceIndex < len(discrimLine):
                discrimPoint = discrimLine[sliceIndex]
                if psd <= discrimPoint:
                    typeSlice += [2]
                elif psd > discrimPoint:
                    typeSlice += [1]
        else:
            typeSlice += [0]

    return slices, typeSlice

def plot(data, xaxis, path):
    fig = plt.figure()
    plt.hist(data.PSD, xaxis)
    plt.xlabel('PSD')
    plt.ylabel('Counts of Particles')
    plt.title('All of the PSD data')
    fig.savefig(path + 'AllData.png')

    fig = plt.figure()
    plt.hist(data[data.particleType == 1].PSD, xaxis)
    plt.xlabel('PSD')
    plt.ylabel('Counts of Particles')
    plt.title('Neutron PSD')
    fig.savefig(path + 'NeutronPSD.png')

    fig = plt.figure()
    plt.hist(data[data.particleType == 2].PSD, xaxis)
    plt.xlabel('PSD')
    plt.ylabel('Counts of Particles')
    plt.title('Photon PSD')
    fig.savefig(path + 'PhotonPSD.png')
