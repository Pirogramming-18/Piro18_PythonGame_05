import requests

cookies = {
    'WMONID': 'sEVAZAA8dcX',
    'ckUserReadTime': '46421347553293697-9352',
    '_ga': 'GA1.1.2057784402.1673103942',
    'WL_PCID': '16731039424508596596795',
    'JSESSIONID': '6F820B3E47D939FBA0891441F08F7AAA.new_portal-svr-11',
    '_ga_0T3XG23CN7': 'GS1.1.1673159915.4.1.1673160248.59.0.0',
}

headers = {
    'Accept': '*/*',
    'Accept-Language': 'ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7',
    'Connection': 'keep-alive',
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    # 'Cookie': 'WMONID=sEVAZAA8dcX; ckUserReadTime=46421347553293697-9352; _ga=GA1.1.2057784402.1673103942; WL_PCID=16731039424508596596795; JSESSIONID=6F820B3E47D939FBA0891441F08F7AAA.new_portal-svr-11; _ga_0T3XG23CN7=GS1.1.1673159915.4.1.1673160248.59.0.0',
    'Origin': 'https://data.seoul.go.kr',
    'Referer': 'https://data.seoul.go.kr/dataList/OA-15442/S/1/datasetView.do',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36',
    'X-Requested-With': 'XMLHttpRequest',
    'sec-ch-ua': '"Not?A_Brand";v="8", "Chromium";v="108", "Google Chrome";v="108"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
}

params = {
    'onepagerow': '1000',
    'srvType': 'S',
    'infId': 'OA-15442',
    'serviceKind': '1',
    'pageNo': '1',
    'gridTotalCnt': '',
    'ssUserId': 'SAMPLE_VIEW',
    'strWhere': '',
    'strOrderby': '',
    'filterCol': '필터선택',
    'txtFilter': '',
}

data = '{"pageNo":"1","pageSize":"10","browser1":"chrome","version":"108","dummy":"A154409760"}'

response = requests.post('https://data.seoul.go.kr/dataList/dataView.do', params=params, cookies=cookies, headers=headers, data=data)
new_str = response.text[87:-6]
# new = json.loads(new_str)
new_str = new_str.split(',')
line_list = [[] for i in range(14)]
list_line = ['경의선', '01호선', '02호선', '03호선', '04호선', '05호선', '06호선', '07호선', '08호선', '09호선', '경춘선', '수인분당선', '공항철도', '신분당선']
for i in range(len(new_str)):
    if new_str[i][:10] == 'STATION_NM':
        line = new_str[i-4][11:-1]
        if line in list_line:
            index_of_line = list_line.index(line)
            line_list[index_of_line].append(new_str[i][12:-1])
print(line_list)



def subway():
    global line_list
    print('-------------------------------------------------------------------------')
    print('경의선: 0   경춘선: 10   수인분당선: 11   공항철도: 12   신분당선: 13')
    print('-------------------------------------------------------------------------')
    subway_num = int(input('지하철~ 지하철! 지하철~ 지하철! 몇호선~ 몇호선? : '))
    print(f'아 {subway_num}호선~ {subway_num}호선!')
    new_list = []
    while True:
        subway_station_name = input('짝짝! : ')
        if subway_station_name not in line_list[subway_num] or subway_station_name in new_list:
            break
        else:
            new_list.append(subway_station_name)
    print('지식은 생명! 지식은 생명!')
    print('생명! 생명! 생명생명생명!')

subway()

