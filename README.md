# Requirements
Python 3.8
Numpy and Matplotlib

# Image-Recognition-without-Neural-Network
After working on a end year project for University, showcasing the better energetic efficiency of Neuromorphic comparing two programms, I've decided to improve my second algorithm. You'll find 3 files of codes : the main programm, the calculation of its accuracy and the test on the MNIST data-base.


The first file PictureRecognition.py is the main program. It contains all the classes required to recognize an image. It is independent to the two other files. I suggest you read carefuly the notes at the beginning.

The two other files are using the MNIST data-base, stored in CSV files. Accuracy.py uses Image_Recognition_MNIST.py in order to calculate the accuracy for a set of data, but it is also independent from the used Data Base. Finally, Image_Recognition_MNIST.py is there in order to open the necessary files containing the MNIST set. 

# Ploting the data
You'll find two (essential) plots. The first one in Image_Recognition_MNIST.py, used to show the charts created for every label. The second one is in Accuracy.py. But be careful with this one : ploting the accuracy depending on the size of the batch AND the precision required by the user might take a while depending on your system. I suggest you first plot it for one value of K (batch size), and some values of delta (threshold). If you feel confident, you can try ploting them all together, and I'd be pleased to see how it looks like on your end. You'll find my own plots in the Plots folder.

# Feedbacks
I'm more than open to feedbacks ! If you have any suggestions that could improve the accuracy, or the time taken to execute please share them ! If you have any questions simply ask and I'll be glad to answer you. I tried to make a very General program in order to be able to use other data and not only the MNIST data-base as I did for my inital University project.

You can join my discord server and send all of this in the Computer-Science channel : https://discord.gg/9WrkhGzy6P
