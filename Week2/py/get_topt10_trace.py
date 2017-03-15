
# coding: utf-8

# In[36]:

import csv
from operator import itemgetter

tashu_dict = csv.DictReader(open('./Data/tashu.csv','r'))
station_dict = csv.DictReader(open('./Data/station.csv','r'))


# In[37]:

trace_count = [[0]*227 for _ in range(227)]

for row in tashu_dict:
    rent_st = row['RENT_STATION']
    return_st = row['RETURN_STATION']

    if rent_st != '' and return_st != '':
        trace_count[int(rent_st)][int(return_st)] += 1


# In[38]:

station_map = {}
for row in station_dict:
    station_map[int(row['키오스크번호'])] = row['명칭']


# In[40]:

station_list = []
for i in range(1,227,1):
    for j in range(1,227,1):
        #print(i,j,trace_count[i][j])
        if trace_count[i][j] > 0:
            station_list.append((i,j,trace_count[i][j]))
            
station_list = sorted(station_list, key=itemgetter(2), reverse=True)


# In[44]:

result = []
top = 0
for i,j,count in station_list:
    if top == 10:
        break
    result.append([station_map[i],str(i),station_map[j],str(j),count])
    top += 1


# In[ ]:



