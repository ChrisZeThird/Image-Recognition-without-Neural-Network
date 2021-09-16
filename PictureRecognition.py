# -*- coding: utf-8 -*-
"""
Created on Sun Sep 12 17:37:21 2021

@author: ChrisZeThird
"""
import numpy as np


"""
The x array mentioned below contains the set of pictures. This array has one dimension (bra type), and contains
the pictures coded in Array. Because this code tries to be a general as possible, I'll consider later that the data set
containing the labels of the training for the creation of the model is stored in a separate array. However, it is likely that :
    
    - The labels and pictures are stored inside the same array, I suggest you either change the code or separate them into two new arrays
    - The pictures are stored in a list as arrays, so you might want to reshape them properly

Some simplifications helped me write this code, in order to be more efficient and focus on more important things. But nothing is eternal so feel
free to make some changes on your own and post a feedback. 
"""

class Recognition():
    
    def __init__(self, x, y, h, w, batch, delta=0.50, p = 255):
        """Input : x -> numpy array of arrays, contains the pictures
                   y -> numpy array of integers, contains the labels
                   h,w -> integers, size of an individual picture from the data base
                   batch -> int, the number of pictures required for the model to be created, must be smaller than the size of x
                   delta -> float, precision of the model, by default is set on 50%
                   p -> integer, by default, the pictures is coded with 255 possible pixel values"""
                       
        self.x = x
        self.y = y
        self.h = h
        self.w = w
        self.batch = batch
        self.delta = delta          
        self.p = p
        
    def normalize(self,x):
        
        """Input : x -> list of arrays, contains the pictures
                   p -> integer, by default, the pictures is coded with 255 possible pixel values
           Output : numpy array of arrays, contains normalized pictures with pixel value of {1,-1} OR {1,0}, feel free to compare those two methods"""
        
        n = len(x)
        x = [(1/self.p)*i for i in x] #first normalization
        for k in range(n):
            a = x[k]
            p,q = a.shape
               
            for i in range(p):
                for j in range(q):
                       
                    if a[i,j] > 0.5 :
                        a[i,j] = 1
                    else:
                        a[i,j] = 0 
                        
        return x
    
    def model(self, x, y, h, w):
        """Input : x -> list of arrays, contains the pictures
                   y -> numpy array of integers, contains the corresponding labels (ket type)
                   h & w -> integers, size of the pictures, necessary for the creation of the reference pictures
           Output : list of arrays, contains the reference picture for every labels"""
        
        x = self.normalize(x)
        #label0 = []
        labels, counts= np.unique(y, return_counts=True) #gets the labels and counts them
        l = len(labels)
        #print(labels)
        #print(counts)
        
        res = [] #creation of a list containing all the reference images
        for z in range(l): #loop on the labels
            res0 = []
            res1 = np.zeros((h,w))
            for i in range(self.batch):
                if y[i,0] == labels[z]: #selection of the images corresponding to the label l
                    a = np.reshape(x[i],(h,w))
                    res0.append(a)
        
            n = len(res0)
    
            #print(res0)
            threshold = (self.delta)*(counts[z])
            for i in range(h): #loop on the pixels
                for j in range(w):
                    c = 0
                    for p in range(n): #loop on the images
                        c += (res0[p])[i,j] #'counter' of the presence of each pixel (fixed) on all images
  
                    if c > threshold :
                        res1[i,j] = 1
                    
            res.append(res1)  
        return res
               
    def prediction(self,image):
        """"Input : image -> np.array, a single image with a size (h,w)
            Output : label corresponding to the input image"""
        temp = [image]
        temp1 = self.normalize(temp)
        image0 = temp1[0]
        
        #print(image0)
        L = self.model(self.x, self.y, self.h, self.w)
        labels= np.unique(self.y, return_counts=False)
        #print(labels)
        N = len(L)
        res0 = [0]*N
        
        for p in range(N):
            for i in range(self.h):
                for j in range(self.w):
                
                    if image0[i,j] == (L[p])[i,j] :
                        res0[p] += 1
                        
        #print(res0)                
        a = max(res0) 
        #print(a)
        b = res0.index(a)
        return labels[b]
        
    
