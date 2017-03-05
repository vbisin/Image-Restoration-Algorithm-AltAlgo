#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 12 14:34:56 2017

@author: vittoriobisin
"""
import numpy as np
def diffOpp(x):
    N=len(x)
    u=np.transpose(np.matrix(np.zeros(N)))
    u[0:N-1]=np.diff(x,axis=0)
    u[N-1]=x[0]-x[N-1]
    return u
    
def diffOppT(x):
    N=len(x)
    u=np.transpose(np.matrix(np.zeros(N)))
    u[0]=x[N-1]-x[0]
    u[1:N]=-np.diff(x,axis=0)
    return u
    