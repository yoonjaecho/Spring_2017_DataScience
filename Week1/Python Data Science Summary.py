
# coding: utf-8

# In[12]:

fam = ['a', 'b', 'c', 'd', 'e', 'f', 'g']


# In[13]:

fam[3:5]


# In[14]:

# [start : end]
# inclusive : exclusive


# In[15]:

fam[:4]


# In[16]:

fam[5:]


# In[17]:

fam[-4:]


# In[19]:

family = fam + ['h', 'i']


# In[36]:

del(family[-1])
family


# In[32]:

x = [1,2,3]
y = x # Deep copy
y[0] = 4
x


# In[35]:

x = [1,2,3]
y = list(x) # or y = x[:]
y[0] = 4
x


# In[42]:

digits = [1,2,3,4,5,6,7,8,9,10]
max(digits)


# In[43]:

round(1.68, 1)


# In[44]:

round(1.68)


# In[46]:

help(round) # open document


# In[56]:

new_digits = sorted(digits, reverse=True)
new_digits 


# In[58]:

fam


# In[59]:

fam.index('g')


# In[62]:

fam += 'g'
fam.count('g')


# In[66]:

sister = 'liz'
sister.capitalize()


# In[71]:

sister.replace('z','sa')


# In[ ]:




# In[72]:

import numpy as np


# In[73]:

np.array([1,2,3])


# In[74]:

from numpy import array


# In[75]:

array([1,2,3])


# In[76]:

fam


# In[78]:

np_fam = array(fam)
np_fam


# In[81]:

import math
from math import radians
r = 192500
dist = r * radians(12)
dist


# In[83]:

'''
Numpy : Numberic Python
Alternative to python list: Numpy array
Calculations over entire arrays
Easy and Fast

Numpy arrays contain only one type
'''


# In[99]:

# height and weight are available as a regular lists

# Import numpy
import numpy as np

height = [150, 160, 170, 180, 190]
weight = [70, 70, 70, 70, 70]

# Calculate the BMI: bmi
np_height_m = np.array(height) * 0.0254
np_weight_kg = np.array(weight) * 0.453592
bmi = np_weight_kg / np_height_m ** 2

# Create the light array
light = bmi < 2

# Print out light
print(light)

# Print out BMIs of all baseball players whose BMI is below 21
print(bmi[light])


# In[100]:

np_list = np.array([1,2,3,4,5])
type(np_list)


# In[101]:

#ndarray = N-dimensional array


# In[102]:

np_list.shape


# In[104]:

np_2d_arr = np.array([[1,2,3],[4,5,6]])


# In[108]:

np_2d_arr[1]


# In[109]:

np_2d_arr[1:,]


# In[111]:

# np_baseball is available

# Import numpy
import numpy as np

np_baseball = np.array([[1,2,3],[4,5,6],[7,8,9]])
# Print mean height (first column)
avg = np.mean(np_baseball[:,0])
print("Average: " + str(avg))

# Print median height. Replace 'None'
med = np.median(np_baseball[:,0])
print("Median: " + str(med))

# Print out the standard deviation on height. Replace 'None'
stddev = np.std(np_baseball[:,0])
print("Standard Deviation: " + str(stddev))

# Print out correlation between first and second column. Replace 'None'
corr = np.corrcoef(np_baseball[:,0],np_baseball[:,1])
print("Correlation: " + str(corr))


# In[112]:

# heights and positions are available as lists

# Import numpy
import numpy as np

heights = [160, 170, 180, 190, 200]
positions = ['FW', 'CB', 'LW', 'RW', 'GK']
# Convert positions and heights to numpy arrays: np_positions, np_heights
np_heights = np.array(heights)
np_positions = np.array(positions)


# Heights of the goalkeepers: gk_heights
gk_heights = np_heights[np_positions == 'GK']

# Heights of the other players: other_heights
other_heights = np_heights[np_positions != 'GK']

# Print out the median height of goalkeepers. Replace 'None'
print("Median height of goalkeepers: " + str(np.median(gk_heights)))

# Print out the median height of other players. Replace 'None'
print("Median height of other players: " + str(np.median(other_heights)))


# In[ ]:



