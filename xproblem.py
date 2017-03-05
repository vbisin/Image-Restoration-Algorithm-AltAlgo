#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 14 16:15:22 2017

@author: vittoriobisin
"""

def xproblem(F):
    
    import scipy.io as sio
    import numpy as np
    from numpy import fft
    
    mat_contents = sio.loadmat('Kfft.mat')
    Kfft=mat_contents["Kfft"]
    mat_contents = sio.loadmat('DtDfft.mat')
    DtDfft=mat_contents["DtDfft"]

    
    KtFfft=np.real(fft.ifft2(np.multiply(np.conj(Kfft),fft.fft2(F))))
    KtKfft=np.abs(Kfft)
    #KtKfft=np.abs(abs((Kfft))+conj(Kfft))
    
    return Kfft,DtDfft,KtFfft,KtKfft
