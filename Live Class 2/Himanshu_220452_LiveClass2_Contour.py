#!/usr/bin/env python
# coding: utf-8

# In[1]:


import cv2
import numpy as np
import matplotlib.pyplot as plt


# In[12]:


img = cv2.imread(r"C:\Users\Himanshu\Downloads\holding-earth-green-tree-hands-world-environment-day-concept-saving-growing-young-tree-element-image-furnished-74844293.jpg")
plt.imshow(img[:,:,::-1]) 
plt.title("Original image") 
plt.axis("Off")


# In[13]:


gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
plt.imshow(gray , cmap='gray')
plt.title("Original image")
plt.axis("Off")


# In[14]:


gray_inv = cv2.bitwise_not(gray)
plt.imshow(gray_inv , cmap='gray')
plt.title("Original image") 
plt.axis("Off")


# In[15]:


contours,hierarchy = cv2.findContours(gray_inv , cv2.RETR_EXTERNAL , cv2.CHAIN_APPROX_NONE)
img_copy = img.copy()
cv2.drawContours(img_copy,contours,-1,(255,0,0),2)
plt.figure(figsize=[10,10])
plt.imshow(img_copy[:,:,::-1])
plt.title("Original image")
plt.axis("Off")


# In[16]:


_, binary = cv2.threshold(gray_inv , 50 ,255 , cv2.THRESH_BINARY)
plt.imshow(binary,cmap='gray');plt.title("Binary image");plt.axis("Off")


# In[21]:


contours,hierarchy = cv2.findContours(binary , cv2.RETR_EXTERNAL , cv2.CHAIN_APPROX_NONE)
img_copy = img.copy()
cv2.drawContours(img_copy,contours,-1,(255,0,0),2)
plt.figure(figsize=[10,10])
plt.imshow(img_copy[:,:,::-1])
plt.title("Original image") 
plt.axis("Off")


# In[ ]:





# In[ ]:




