#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#importing the required packs
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os
import cv2
from sklearn import svm, datasets
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.utils import shuffle
from sklearn.metrics import classification_report,accuracy_score


# In[ ]:


#1. IMAGE PRE-PROCESSING
#The actions in this section will help the main SVM model to work with the images provided and preferably also reduce the
# size/shape of the data so that the memory of the code will not exceed the limit Jupyter Notebook has. 

#Creating a path for the source dataset (which are the images) and storing it in a list.
path=(r"C:\Users\melek\OneDrive\Belgeler\Year 4\AMLS\CW\dataset\image")
images_list= []
images_paths = sorted(list(paths.list_images(path)))

#One of our first tasks will be to convert the pixels of the images into an array form. 
#To do this, we must first make sure that the images provided are in grayscale.
for path inn images_paths:
    images_file = cv2.imread(path)
    gray = cv.cvtColor(image_file,cv2.COLOR_BGR2GRAY)
    images_list.append(gray)
    

    


# In[ ]:


#This prepares the labels so they can be processed: 
labeldata = pd.read_csv(r"C:\Users\melek\OneDrive\Belgeler\Year 4\AMLS\CW\dataset\label.csv")
X = []
Y = []


# In[ ]:


X = np.array(X)
X_reshaped=X.reshape(len(X),-1)


# In[ ]:


#The provided images are classified into a binary classification (with and without tumor)
#Whenever there is "no_tumor" in the label, the image will be classified into 0, and into 1 if it is the other way around
for i in range (0,3000):
    X.append(images_list[i])
    if "no_tumor" in (labeldata.iat[i,1]):
        Y.append(0)
    else:
        Y.append(1)

