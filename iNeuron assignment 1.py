#!/usr/bin/env python
# coding: utf-8

# solution 1 :
# 

# In[3]:


for i in range(2000,3201):
    if i%7==0:
        if i%5==1:
            print(i,end=",")


# solution 2 :

# In[6]:


f_name = input("Enter your name :")
l_name = input("Enter your last name :")
print("{} {}".format(f_name[::-1],l_name[::-1]))


# solution 3 :
# 

# In[8]:


import math as mt
diameter=12
r=diameter/2
volume = 4/3 * mt.pi * mt.pow(r,3)
print("volume of sphare with diameter {} is {}".format(diameter,volume))


# In[ ]:




