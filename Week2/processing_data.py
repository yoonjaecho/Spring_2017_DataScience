# coding: utf-8
import csv

result = []

with open('./Data/2015_02_tashu.csv','r') as f:
    content = csv.reader(f, delimiter=',')
    for row in content:
        for str in range (len(row)):
            row[str] = row[str].replace("'",'')
        result.append(row)
f.close()

with open('./Data/output_2015_02_tashu.csv','w') as ff:
    writer = csv.writer(ff, delimiter=',')
    for rows in result:
        writer.writerow(rows)
ff.close()
