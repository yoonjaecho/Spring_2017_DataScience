import csv
from operator import itemgetter

def get_top10_station(tashu_dict, station_dict):
    
    station_cnt = [0] * (226 + 1)

    for row in tashu_dict:
        rent_index = row['RENT_STATION']
        return_index = row['RETURN_STATION']
        if rent_index == '' or return_index == '':
            continue
        station_cnt[int(rent_index)] += 1
        station_cnt[int(return_index)] += 1

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


def get_top10_trace(tashu_dict, station_dict):
    
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
