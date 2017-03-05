#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 14 16:11:11 2017

@author: vittoriobisin
"""

def altAlgo(convolvedNoise,realSignal,mu):
    
    import numpy as np   
    from diffOpp import diffOpp,diffOppT
    from numpy import fft 
    from xproblem import xproblem
    import scipy.stats

    #kernel=np.transpose(np.matrix(kernel[:200]))
    
    m=len(convolvedNoise)
    
    ##Initialization 
    
    lam1=np.transpose(np.matrix(np.zeros(m)))
    beta=10.
    gamma=1.618
    #mu=50000.
    MSE=list()
    SNR=list()
    SAD=list()
    x=convolvedNoise
    
    ## Finite difference
    D1x=diffOpp(x)
    w=np.transpose(np.matrix(np.zeros(len(x))))
    Kfft,DtDfft,KtFfft,KtKfft=xproblem(convolvedNoise)
    ## Main Loop
    
    for i in range(0,250):
        
        
        # i) Shrinkage (i.e. minimizing y, which is "w" in the paper)
        
        Z1=D1x + lam1/beta
        V=np.abs(Z1)
        for j in range(0,len(x)):
            if V[j]==0:
                V[j]=1
            V[j]=np.max(V[j]-(1./beta),0)/V[j]
        w=np.multiply(Z1,V)

        
        
        #ii) FFT (i.e. minimizing u)
        x=(mu*KtFfft-diffOppT(lam1))/beta+diffOppT(w)
        denom=DtDfft+(mu/beta)*KtKfft
        x=np.divide(fft.fft2(x),denom)
        x=np.real(fft.ifft2(x))
        
        
        
        # iii) Finite differences
        MSE.append(sum(((np.square(x[100:1100,:]-realSignal[100:1100,:]))))/np.float64(1000))
        SNR.append(scipy.stats.signaltonoise(x[100:1100,:]))
        SAD.append(sum(abs(x[100:1100,:]-realSignal[100:1100,:])))
        D1x=diffOpp(x)
        
        
        # iv) update lam
        lam1=lam1-gamma*beta*(w-D1x)
    
    return (x,MSE,SNR,SAD)    
    
    
    
    
        
        
        
        
