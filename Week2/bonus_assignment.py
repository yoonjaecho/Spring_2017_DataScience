import csv
import pandas as pd
from operator import itemgetter
import pylab
import datetime
import numpy
import matplotlib.image
import matplotlib.pyplot as plt
from matplotlib import font_manager, rc
from operator import itemgetter
import numpy as np
from numpy import *

tashu = pd.read_csv('tashu.csv', dtype={'RENT_DATE': str, 'RETURN_DATE': str})
station = pd.read_csv('./station.csv')

kiosk_per_district_count = station.groupby('구별').키오스크번호.count()

plt.title('Number of stations per district')
kiosk_per_district_count.plot(kind='bar');
plt.axhline(0, color='k')
plt.rc('font', family='AppleMyungjo')
plt.show()

kiosk_district_dict = dict(zip(station.키오스크번호, station.구별))

# Data cleansing
tashu = tashu.dropna()
tashu['RENT_DATE'] = pd.to_datetime(tashu['RENT_DATE'], format = '%Y%m%d%H%M%S')
tashu['RETURN_DATE'] = pd.to_datetime(tashu['RETURN_DATE'], format = '%Y%m%d%H%M%S')
tashu[:10]

usage_per_district = {}
for usage in tashu['RENT_STATION']:
    if usage in kiosk_district_dict:
        if kiosk_district_dict[usage] in usage_per_district:
            usage_per_district[kiosk_district_dict[usage]] += 1
        else:
            usage_per_district[kiosk_district_dict[usage]] = 1
     
usage_per_district

X = np.arange(len(usage_per_district))
plt.bar(X, usage_per_district.values(), align='center', width=0.5)
plt.xticks(X, usage_per_district.keys())
plt.title('Number of usage per district')
plt.rc('font', family='AppleMyungjo')
plt.show()

tashu['weekday'] = pd.DatetimeIndex(tashu['RENT_DATE']).weekday
weekday = tashu.groupby('weekday').RENT_STATION.count()
weekday

plt.title('Day of A Week Transaction')
weekday.plot(kind='bar'); plt.axhline(0, color='k')
plt.xticks((0,1,2,3,4,5,6),('Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun'))
plt.show()

y_hour_count = [0] * 24

for rent_time in tashu['RENT_DATE']:
    y_hour_count[rent_time.hour] += 1
    
x_hour = []
for i in range(0,24,1):
    x_hour.append(i)

print('\n'.join('{}: {}'.format(*k) for k in enumerate(y_hour_count)))

plt.xticks(np.arange(0, max(x_hour)+1, 1.0))
plt.title("Usage per hour")
plt.bar(range(len(y_hour_count)), y_hour_count, 0.5, color="blue", align="center")

weekday_usage = [[],[],[],[],[],[],[]]
asdf = 0
for row in tashu['RENT_DATE']:
    weekday_usage[row.weekday()].append(row.hour)

weekday_usage_hour_count = [[],[],[],[],[],[],[]]

for i in range(0,7,1):
    for j in range(0,24,1):
        weekday_usage_hour_count[i].append(weekday_usage[i].count(j))

plt.xticks(np.arange(0, 24, 1))
plt.title("Day-hour usage pattern")

ax = plt.subplot(111)
dates = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
i=0
for day_hour in weekday_usage_hour_count:
    plt.plot(day_hour, label=dates[i])
    i+=1
    
ax.legend(loc='center left', bbox_to_anchor=(1, 0.5))

