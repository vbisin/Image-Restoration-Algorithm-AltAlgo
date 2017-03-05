#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 15 16:15:21 2017

@author: vittoriobisin
"""

def blurAltAlgo (t,realSignal):
    
    import numpy as np
    from extra import convmtx
    from kernel import gauss
    
    #Correct Gaussian Kernel 
    gaussian=gauss(100,10)
    gaussian=gaussian[1:len(gaussian)]

    #Get gauss filter 
    
    
    #Solving bam via convmtx
    bam=convmtx(gaussian,1200)
    bam=bam[:,50:1250]
    noise = np.transpose(np.matrix(np.random.normal(0,1,1200)))
    
    convolvedNoise=bam*realSignal+noise
#    
    return convolvedNoise
#   