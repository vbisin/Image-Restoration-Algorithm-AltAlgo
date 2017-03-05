#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 14 16:42:12 2017

@author: vittoriobisin
"""

def bestMu(convolvedNoise,realSignal):
    from altAlgo import altAlgo
    import numpy as np
    
    interval=np.float64(range(15,30))
    interval=1.5**interval
    best=np.transpose(np.matrix(np.ones(1200))*10)
    optMu=1
    
    for mu in interval:
        (estimate,MSE,SNR,SAD)=altAlgo(convolvedNoise,realSignal,mu)
    
        if sum(abs(estimate[100:1100,:]-realSignal[100:1100,:]))<sum(abs(best[100:1100,:]-realSignal[100:1100,:])):
            best=estimate
            optMu=mu
    
    return optMu