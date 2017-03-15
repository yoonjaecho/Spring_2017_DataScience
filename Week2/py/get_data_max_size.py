
# coding: utf-8

# In[3]:

import csv
tashu_dict = csv.DictReader(open('./Data/tashu.csv','r'))


# In[4]:

max_size = 0

for row in tashu_dict:
    index = row['RENT_STATION']
    if index != '':
        max_size = max(max_size, int(index))
        
    index = row['RETURN_STATION']
    if index != '':
        max_size = max(max_size, int(index))
        
print(max_size)

