#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 16 16:10:10 2017

@author: vittoriobisin
"""
import scipy.io as sio
import numpy as np
from numpy import fft
import cv2


mat_contents = sio.loadmat('mse.mat')
mse=mat_contents["mse"]
    
mat_contents = sio.loadmat('Bn.mat')
Bn=mat_contents["Bn"]


mat_contents = sio.loadmat('I.mat')
I=mat_contents["I"]


mat_contents = sio.loadmat('sol.mat')
sol=mat_contents["sol"]

mat_contents = sio.loadmat('SAD.mat')
SAD=mat_contents["SAD"]

cv2.imshow('image',I)
cv2.imwrite('originalImage.png',I)

cv2.imshow('image',Bn)
cv2.imwrite('ConvolvedandNoisyImage.png',Bn)

cv2.imshow('image',sol)
cv2.imwrite('recoveredImage.png',sol)

preimage=np.arange(9)+1

plt.figure(1)
line1=plt.plot(preimage,mse,'r',label='Convolved Signal')
plt.title("MSE of 2D Amarcord Image")
plt.xlabel('Iterations')
plt.ylabel('MSE')
plt.savefig("MSE2D")
plt.show


plt.figure(2)
line1=plt.plot(preimage,SAD,'r',label='Convolved Signal')
plt.title("SAD of 2D Amarcord Image")
plt.xlabel('Iterations')
plt.ylabel('SAD')
plt.savefig("SAD3d")
plt.show