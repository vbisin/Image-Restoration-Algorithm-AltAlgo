

from bestMu import bestMu
import numpy as np
from blurAltAlgo import blurAltAlgo
from altAlgo import altAlgo
import matplotlib.pyplot as plt

## Setting up signal 

# Sampling frequency     
Fs = 1000.0
# Sampling period                            
T = 1.0/Fs           
# Time vector
t= np.zeros(1000)
for i in range (0,1000):
    t[i]=(i*T)    


## Real signal: step function 
realSignal=np.zeros(1200)
realSignal[0:200]=0
realSignal[200:300]=20
realSignal[300:400]=30
realSignal[400:500]=40
realSignal[500:700]=50
realSignal[700:800]=70        
realSignal[800:900]=80
realSignal[900:1200]=100

realSignal=np.transpose(np.matrix(realSignal))    

        
convolvedNoise=blurAltAlgo(t,realSignal)

optMu=bestMu(convolvedNoise,realSignal)
#optMu=1.5**23
(recoveredSignal,MSE,SNR,SAD)=altAlgo(convolvedNoise,realSignal,optMu)


# Graphs
preimage=np.arange(250)

convolvedNoise=convolvedNoise[100:1100,:]
realSignal=realSignal[100:1100,:]
recoveredSignal=recoveredSignal[100:1100,:]



plt.figure(1)
line1=plt.plot(t,realSignal,'r',label='Original Signal')
plt.plot(t,convolvedNoise,'b',label='Convolved Noisy Signal')
plt.legend(bbox_to_anchor=(.46, .99), loc=0, borderaxespad=0.)
plt.title("Original and Convolved Noisy Signals")
#plt.savefig('Original and Convolved Noisy Signals')
plt.show

plt.figure(2)
line1=plt.plot(t,realSignal,'r',label='Original Signal')
plt.plot(t,recoveredSignal,'k',label='Recovered Signal')
plt.legend(bbox_to_anchor=(.38, .99), loc=0, borderaxespad=0.)
plt.title("Original and Recovered Signals")
#plt.savefig('Original and Recovered Signals')
plt.show



plt.figure(3)
line1=plt.plot(t,convolvedNoise,'r',label='Convolved Noisy Signal')
plt.plot(t,recoveredSignal,'k',label='Recovered Signal')
plt.legend(bbox_to_anchor=(.46, .99), loc=0, borderaxespad=0.)
plt.title("Convolved Noisy and Recovered Signals")
#plt.savefig('Original and Recovered Signals')
plt.show




plotMSE=np.zeros(250)
plotSNR=np.zeros(250)
plotSAD=np.zeros(250)
for i in range(0,250):
    plotMSE[i]=MSE[i].item()
    plotSNR[i]=SNR[i].item()
    plotSAD[i]=SAD[i].item()

plt.figure(4)
line1=plt.plot(preimage,plotMSE)
plt.xlabel('Iterations')
plt.ylabel('MSE')
plt.title("MSE of Alternating Algorithm")
#plt.savefig("MSE of Alternating Algorithm")
plt.show

plt.figure(5)
line1=plt.plot(preimage,plotSAD)
plt.xlabel('Iterations')
plt.ylabel('Sum of Absolute Differences')
plt.title("SAD of Alternating Algorithm")
#plt.savefig("SAD of Alternating Algorithm")
plt.show

import pylab
plt.figure(6)
line1=plt.plot(preimage,SNR)
plt.xlabel('Iterations')
plt.ylabel('SNR')
pylab.ylim([1.7,1.715])
plt.title("SNR of Alternating Algorithm")
#plt.savefig("SNR of Alternating Algorithm")
plt.show


#
#plt.figure(7)
#line1=plt.plot(t,convolved,'r',label='Convolved Signal')
#line2=plt.plot(t,recoveredSignal,'b',label='Recovered Signal')
#plt.legend(bbox_to_anchor=(.98, .98), loc=0, borderaxespad=0.)
#plt.title("Convolved and Recovered Signal")
##plt.savefig("Convolved and Recovered Signal")
#plt.show

