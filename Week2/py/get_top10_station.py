
# coding: utf-8

# In[1]:

import csv
from operator import itemgetter


# In[2]:

station_cnt = [0] * (226 + 1)


# In[4]:

tashu_dict = csv.DictReader(open('./Data/tashu.csv','r'))
for row in tashu_dict:
    rent_index = row['RENT_STATION']
    return_index = row['RETURN_STATION']
    if rent_index == '' or return_index == '':
        continue
    station_cnt[int(rent_index)] += 1
    station_cnt[int(return_index)] += 1


# In[5]:

station_dict = csv.DictReader(open('./Data/station.csv','r'))
station_map = {}
for row in station_dict:
    station_map[int(row['키오스크번호'])] = row['명칭']


# In[6]:

station_list = []
for index in range(len(station_cnt)):
    station_list.append((index, station_cnt[index]))
station_list = sorted(station_list, key=itemgetter(1), reverse=True)


# In[7]:

result = []
top = 0
for kioki,cnt in station_list:
    if top == 10:
        break
    result.append([station_map[int(kioki)], str(kioki), cnt])
    top += 1

print(result)


# In[ ]:



