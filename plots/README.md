# What are those plots ?

In this folder you'll find two different types of plots :

  1- The differents charts obtained with variable values of delta, for a batch size K = 1000

  2- Two plots the the Accuracy folder, showing the accuracy obtaines for different batch size (100, 200, 500, 1000) for a fixed value of delta

For the Accuracy plots, you'll notice a big change of the maximum accuracy obtained. This is explained by the changes made in the normalization function in PictureRecognition.py. I invite you to change thz values of empty pixel from 0 to -1, and vice versa.
It is truly remarquable to see that a {-1,1} normalization as I like to call it, results in a better accuracy for relatively small batch size.

# What are those names ?

The file name gives you information about the delta value used, and the normalization method ({0,1} or {-1,1}). Just know that the charts you observe are being plots for a batch size of 1000. 
