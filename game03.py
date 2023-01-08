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
new_str = new_str.split(',')
list_subway = [[] for i in range(14)]
list_line = ['경의선', '01호선', '02호선', '03호선', '04호선', '05호선', '06호선', '07호선', '08호선', '09호선', '경춘선', '수인분당선', '공항철도', '신분당선']

# 크롤링 데이터를 list_subway에 저장하기
for i in range(len(new_str)):
    if new_str[i][:10] == 'STATION_NM':
        line = new_str[i-4][11:-1]
        if line in list_line:
            index_of_line = list_line.index(line)
            list_subway[index_of_line].append(new_str[i][12:-1])
print(list_subway)

def game03():
    # main에서 크롤링한 데이터 가져오기
    global list_subway
    print('-------------------------------------------------------------------------')
    print('경의선: 0   경춘선: 10   수인분당선: 11   공항철도: 12   신분당선: 13')
    print('-------------------------------------------------------------------------')
    try:
        # intro
        subway_num = int(input('지하철~ 지하철! 지하철~ 지하철! 몇호선~ 몇호선? : '))
        if subway_num < 0 or subway_num > 13: 
            while True:
                print('0 ~ 13 사이의 숫자만 입력해주세요!!')
                subway_num = int(input('지하철~ 지하철! 지하철~ 지하철! 몇호선~ 몇호선? : '))
                if 0 <= subway_num <= 13:
                    break
    except Exception as e:
        print(e)
    else:
        print(f'아 {subway_num}호선~ {subway_num}호선!')
        # 반복된 지하철역 있는지 확인하는 리스트
        new_list = []
        # 몇번 성공적으로 진행됐는지 확인하는 변수
        count = 0
        while True:
            subway_station_name = input('짝짝! : ')
            if subway_station_name not in list_subway[subway_num] or subway_station_name in new_list:
                break
            else:
                new_list.append(subway_station_name)
                count+=1
        print('지식은 생명! 지식은 생명!')
        print('생명! 생명! 생명생명생명!')
        # return된 값으로 술마시고 다음 게임을 진행할 사람을 정한다
        # count가 0이면 같은 사람이 다음 게임 시작
        # count가 1이면 리스트에 저장된 순서의 다음 사람이 게임 시작
        return count

game03()

