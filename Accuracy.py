# -*- coding: utf-8 -*-
"""
Created on Tue Sep 14 15:25:24 2021

@author: ChrisZeThird
"""

"""Separated file, meant to calculate the accuracy of the PictureRecognition programm, for different values of:
    - K : the size of the batch
    - delta : the precision 
    
   The goal is to plot thanks to matplotlib, the evolution of the accuracy depending on K and delta, in order to maximise it."""
   
   
import numpy as np
import matplotlib.pyplot as plt
import PictureRecognition_Numpy_Improved as pr
import Image_Recognition_MNIST as irm
import time

"""Accuracy calculation"""

def accuracy(x,y,K,delta):
    """Input -> x : list of numpy array, contains the pictures
                y : numpy array, contains the labels
                K : integer, gives the size of the batch studied
                delta : flot, precision given by the user, with delta in [0,1]
       Output -> float, gives the accuracy of the programm"""
    res0 = np.array([])   
    R = pr.Recognition(x, y, 28, 28, K, delta)   
    for k in range(K):
        res0 = np.append(res0,R.prediction(x[k]))
        
    res = np.reshape(res0,(K,1))
    
    c = np.sum(res==y[:K,])
    
    return np.average(c)
"""Variable call"""

x = irm.x
y = irm.y

"""PLotting of the different accuracy for various batch and threshold values"""

K_array = np.linspace(start=100,stop=1000,num=5, dtype=int) #Array of different sizes of batches
Delta = np.linspace(start=0,stop=1,num=5,endpoint=False, dtype=float) #Array of different threshold values

acc_per_batch = np.array([])
Time = []

for a in np.nditer(K_array):
    acc_per_thres = np.array([])   
    ping = time.time()
    for b in np.nditer(Delta):
        acc = accuracy(x, y, a, b)
        acc_per_thres = np.append(acc_per_thres,acc)
    
    acc_per_batch = np.append(acc_per_batch,acc_per_thres)    
    pong = time.time()
    Time.append(pong-ping)
    
# n = K_array.size()
# fig, axs = plt.subplots(n, figsize=(16,9))    
# fig.suptitle('Accuracy for different batch values', fontsize=16)

# for k in range(n):
#     a = axs[k]
#     a.plot(Delta,res0[k])
#     a.title.set_text("Batch of" + str(axs[k]) + "pictures")
#     a.suptitle.set_text("Realized in " + str(T[k]) + " seconds")
#     a.set_xlabel("Threshold")
#     a.set_ylabel("Accuracy")

# plt.show()   
    


