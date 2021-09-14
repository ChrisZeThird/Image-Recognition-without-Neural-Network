# -*- coding: utf-8 -*-
"""
Created on Sun Sep 12 21:38:01 2021

@author: ChrisZeThird
"""

"""Application of the PictureRecognition programm on the MNIST data base"""


import numpy as np
#import matplotlib.pyplot as plt
import PictureRecognition as pr
#import time

#ping = time.time()


data = open('train.csv','r')

data_np = np.genfromtxt(data, delimiter=",")

x0 = data_np[1:2001,1:]
y = np.reshape(data_np[1:1001,0],(1000,1))

K = 1000

x = []

for k in range(K):
    x1 = np.reshape(x0[k,],(28,28))
    x.append(x1)
    
    #print(x[k]) 
#print(x)    

R = pr.Recognition(x, y, 28, 28, K, 0.60)
#print(R.normalize(x))
M = R.model(x, y, 28, 28)
#print(R.prediction(x[2]))

#pong = time.time()
#print(pong - ping)


"""Graphic Visualisation with matplotlib"""

# fig = plt.figure(figsize=(16,9))
# ax1 = fig.add_subplot(2, 5, 1)
# ax2 = fig.add_subplot(2, 5, 2)
# ax3 = fig.add_subplot(2, 5, 3)
# ax4 = fig.add_subplot(2, 5, 4)
# ax5 = fig.add_subplot(2, 5, 5)
# ax6 = fig.add_subplot(2, 5, 6)
# ax7 = fig.add_subplot(2, 5, 7)
# ax8 = fig.add_subplot(2, 5, 8)
# ax9 = fig.add_subplot(2, 5, 9)
# ax10 = fig.add_subplot(2, 5, 10)

# ax1.set_ylabel('Label : 0', fontsize=9)
# t0 = M[0]
# ax1.axis('off')
# ax1.imshow(t0, cmap = 'gray_r')

# ax2.set_ylabel('Label : 1', fontsize=9)
# t1 = M[1]
# ax2.axis('off')
# ax2.imshow(t1, cmap = 'gray_r')

# ax3.set_ylabel('Label : 2', fontsize=9)
# t2 = M[2]
# ax3.axis('off')
# ax3.imshow(t2, cmap = 'gray_r')

# ax4.set_ylabel('Label : 3', fontsize=9)
# t3 = M[3]
# ax4.axis('off')
# ax4.imshow(t3, cmap = 'gray_r')

# ax5.set_ylabel('Label : 4', fontsize=9)
# t4 = M[4]
# ax5.axis('off')
# ax5.imshow(t4, cmap = 'gray_r')

# ax6.set_ylabel('Label : 5', fontsize=9)
# t5 = M[5]
# ax6.axis('off')
# ax6.imshow(t5, cmap = 'gray_r')

# ax7.set_ylabel('Label : 6', fontsize=9)
# t6 = M[6]
# ax7.axis('off')
# ax7.imshow(t6, cmap = 'gray_r')

# ax8.set_ylabel('Label : 7', fontsize=9)
# t7 = M[7]
# ax8.axis('off')
# ax8.imshow(t7, cmap = 'gray_r')

# ax9.set_ylabel('Label : 8', fontsize=9)
# t8 = M[8]
# ax9.axis('off')
# ax9.imshow(t8, cmap = 'gray_r')

# ax10.set_ylabel('Label : 9', fontsize=9)
# t9 = M[9]
# ax10.axis('off')
# ax10.imshow(t9, cmap = 'gray_r')

# plt.show()

""""Checking manually the accuracy on few values"""

# pred = []
# for k in range(20):
#     pred.append(float(R.prediction(x[k])))
# print(np.asarray(pred))
# print(y[:20,0])  