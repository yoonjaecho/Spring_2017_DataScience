
# coding: utf-8

# In[2]:

import csv
from operator import itemgetter


# In[5]:

def get_top10_station(tashu_dict, station_dict):
    """
    [역할]
    정류장 Top10 출력하기
    대여 정류장과 반납정류장을 합한 총 사용빈도수 Top10
    """

    """
    [입력]
    tashu_dict : csv.DictReader 형태의 타슈대여정보
    station_dict : csv.DictReader 형태의 정류장 정보
    """

    """
    [출력]
    Top10 정류장 리스트
    ex.) [[정류장 이름1, 정류장 번호1, 정류장1 count], [정류장 이름2, 정류장 번호2, 정류장2 count], .....] 형태
    """
    
    station_cnt = [0] * (226 + 1)
    for row in tashu_dict:
        index = row['RENT_STATION']
        if index != '':
            station_cnt[int(index)] += 1

        index = row['RETURN_STATION']
        if index != '':
            station_cnt[int(index)] += 1
            

    station_map = {}
    for row in station_dict:
        station_map[int(row['키오스크번호'])] = row['명칭']
    
    station_list = []
    for index in range(len(station_cnt)):
        station_list.append((index, station_cnt[index]))
    station_list = sorted(station_list, key=itemgetter(1), reverse=True)
    
    result = []
    top = 0
    for kioki,cnt in station_list:
        if top == 10:
            break
        result.append([station_map[int(kioki)], str(kioki), cnt])
        top += 1
    
    return result


# In[7]:

def get_top10_trace(tashu_dict, station_dict):
    """
    [역할]
    경로 Top10 출력하기
    (대여정류장, 반납정류장)의 빈도수 Top10

    [입력]
    tashu_dict : csv.DictReader 형태의 타슈대여정보
    station_dict : csv.DictReader 형태의 정류장 정보

    [출력]
    Top10 경로 리스트
    ex.) [[출발정류장 이름1, 출발정류장 번호1, 반납정류장 이름1,
        반납정류장 번호2, 경로 count], [출발정류장 이름2, 출발정류장 번호2,
        반납정류장 이름2,  반납정류장 번호2, 경로count2], .....] 형태
    """
    
    trace_count = [[0]*227 for _ in range(227)]

    for row in tashu_dict:
        rent_st = row['RENT_STATION']
        return_st = row['RETURN_STATION']

        if rent_st != '' and return_st != '':
            trace_count[int(rent_st)][int(return_st)] += 1
            
            
    station_map = {}
    
    for row in station_dict:
        station_map[int(row['키오스크번호'])] = row['명칭']
        
    station_list = []
    for i in range(1,227,1):
        for j in range(1,227,1):
            #print(i,j,trace_count[i][j])
            if trace_count[i][j] > 0:
                station_list.append((i,j,trace_count[i][j]))

    station_list = sorted(station_list, key=itemgetter(2), reverse=True)


    result = []
    top = 0
    for i,j,count in station_list:
        if top == 10:
            break
        result.append([station_map[i],str(i),station_map[j],str(j),count])
        top += 1
    
    return result


# In[ ]:



