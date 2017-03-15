import unittest
from homework_tashu import *
# 데이터 클렌징 테스트
class Test(unittest.TestCase):

    def setUp(self):
        self.tashu_file = open('tashu.csv','r')
        self.station_file = open('station.csv','r')

        self.tashu_dict = csv.DictReader(self.tashu_file)
        self.station_dict = csv.DictReader(self.station_file)

    def tearDown(self):
        self.tashu_file.close()
        self.station_file.close()
 
    def test_get_top10_station(self):
        answer = [\
        [' 한밭수목원(정문입구)', '3', 348977],\
        [' 충대정문(장대네거리)', '56', 182114],\
        ['유성구청', '31', 166866],\
        ['타임월드 앞 ', '17', 165778],\
        [' 홈플러스(유성점)', '32', 147063],\
        ['월평역', '33', 142310],\
        ['둔산 하이마트 앞', '14', 114878],\
        ['카이스트 서쪽 쪽문', '105', 112921],\
        ['카이스트 학사식당 앞', '21', 111715],\
        [' 충대정문오거리 1', '55', 110045]\
        ] 
       
        result = get_top10_station(self.tashu_dict, self.station_dict)
        self.assertEqual(result, answer)

    def test_get_top10_trace(self):
        answer = [\
        [' 한밭수목원(정문입구)', '3', ' 한밭수목원(정문입구)', '3', 84496],\
        ['유성구청', '31', '유성구청', '31', 21749],\
        [' 충대정문(장대네거리)', '56', ' 충대정문(장대네거리)', '56', 18343],\
        ['카이스트 학사식당 앞', '21', '카이스트 서쪽 쪽문', '105', 17220],\
        ['무역전시관입구(택시승강장 앞)', '1', '무역전시관입구(택시승강장 앞)', '1', 14489],\
        [' 홈플러스(유성점)', '32', ' 홈플러스(유성점)', '32', 12177],\
        ['카이스트 서쪽 쪽문', '105', '카이스트 학사식당 앞', '21', 12154],\
        ['월평역', '33', '월평역', '33', 11973],\
        ['타임월드 앞 ', '17', '타임월드 앞 ', '17', 11966],\
        [' 충대정문(장대네거리)', '56', ' 홈플러스(유성점)', '32', 11868],\
        ]
       
        result = get_top10_trace(self.tashu_dict, self.station_dict)

        self.assertEqual(result, answer)

if __name__ == '__main__':
    unittest.main()




