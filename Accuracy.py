# -*- coding: utf-8 -*-
"""
Created on Tue Sep 14 15:25:24 2021

@author: ChrisZeThird
"""

"""Separated file, meant to calculate the accuracy of the PictureRecognition programm, for different values of:
    - K : the size of the batch
    - delta : the precision 
    
   The goal is to plot thanks to matplotlib, the evolution of the accuracy depending on K and delta, in order to maximise it."""
   
   

import matplotlib.pyplot as plt
import PictureRecognition as pr
import Image_Recognition_MNIST as irm


"""Accuracy calculation"""

def accuracy(x,y,K,delta):
    """Input -> x : list of numpy array, contains the pictures
                y : numpy array, contains the labels
                K : integer, gives the size of the batch studied
                delta : flot, precision given by the user, with delta in [0,1]
       Output -> float, gives the accuracy of the programm"""
       
    R = pr.Recognition(x, y, 28, 28, K, delta)   
    result = [0]*K
    
    for k in range(K):
        p = R.prediction(x[k])
        if p == y[k,0]:
            result[k] = 1
    
    return sum(result)/K
       
"""Variable call"""

x = irm.x
y = irm.y

"""PLotting of the different accuracy"""

delta_list = [0.70, 0.80, 0.90] #list of different threshold values
K_list = [100, 200, 500, 1000] #list of different size of batches

acc_list100 = []
acc_list200 = []
acc_list500 = []
acc_list1000 = []

K0 = 100
K1 = 200
K2 = 500
K3 = 1000

for n in range(3):
    
    delta0 = delta_list[n]
    a0 = accuracy(x, y, K0, delta0)
    a1 = accuracy(x, y, K1, delta0)
    a2 = accuracy(x, y, K2, delta0)
    a3 = accuracy(x, y, K3, delta0)
    acc_list100.append(a0)
    acc_list200.append(a1)
    acc_list500.append(a2)
    acc_list1000.append(a3)

#setting plot
fig = plt.figure(figsize=(16,9))
ax1 = fig.add_subplot(2, 2, 1)
ax2 = fig.add_subplot(2, 2, 2)
ax3 = fig.add_subplot(2, 2, 3)
ax4 = fig.add_subplot(2, 2, 4)

ax1.set_ylabel('Accuracy', fontsize=9)
ax1.set_xlabel('Threshold', labelpad = 9)
ax1.bar(delta_list,acc_list1000)

ax2.set_ylabel('Accuracy', fontsize=9)
ax2.set_xlabel('Threshold', labelpad = 9)
ax2.plot(delta_list,acc_list200)

ax3.set_ylabel('Accuracy', fontsize=9)
ax3.set_xlabel('Threshold', labelpad = 9)
ax3.plot(delta_list,acc_list500)

ax4.set_ylabel('Accuracy', fontsize=9)
ax4.set_xlabel('Threshold', labelpad = 9)
ax4.plot(delta_list,acc_list1000)

plt.show()

