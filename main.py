import random
import sys
import requests
# 게임에 참여하는 유저 클래스


def game01(players, starter):
    print('''
    ■■■■■■■□■□□□□□■□□■■■■■■□□□□□□□■■■■■■□□□□■■□□□□■■□□□□□■■□□■■■■■■□□□□□□□■■■■■■□□■■■■■■□□□□□■■■■■■□□□■■■■■■□□□□■■□□□■■■■■■■□■□□□□□■
    □□□■□□□□■□□□□□■□□■□□□□□□□□□□□■■■□□■■□□□□■■■□□□■■□□□□□■■□□■□□□□□□□□□□□■■■□□■■■□■□□□□□□□□□□■□□□■■■□□■□□□□□□□□□■■■□□□□□■□□□□■□□□□□■
    □□□■□□□□■□□□□□■□□■□□□□□□□□□□□■■□□□□□□□□■■■■□□□■■■□□□■■■□□■□□□□□□□□□□□■■□□□□■■□■□□□□□□□□□□■□□□□■■□□■□□□□□□□□■■■■□□□□□■□□□□■□□□□□■
    □□□■□□□□■■■■■■■□□■□□□□□□□□□□□■□□□□□□□□□■□□■□□□■■■□□□■■■□□■□□□□□□□□□□□■□□□□□□■□■□□□□□□□□□□■□□□□□■□□■□□□□□□□□■□□■□□□□□■□□□□■■■■■■■
    □□□■□□□□■□□□□□■□□■■■■■■□□□□□□■□□■■■■□□■■□□■■□□■□■■□■■□■□□■■■■■■□□□□□□■□□□□□□■□■■■■■■□□□□□■□□□□□■□□■■■■■■□□■■□□■■□□□□■□□□□■□□□□□■
    □□□■□□□□■□□□□□■□□■□□□□□□□□□□□■□□□□□■□□■■■■■■□□■□□■□■□□■□□■□□□□□□□□□□□■□□□□□□■□■□□□□□□□□□□■□□□□□■□□■□□□□□□□■■■■■■□□□□■□□□□■□□□□□■
    □□□■□□□□■□□□□□■□□■□□□□□□□□□□□■■□□□□■□□■□□□□■■□■□□■■■□□■□□■□□□□□□□□□□□■■□□□□■■□■□□□□□□□□□□■□□□□■■□□■□□□□□□□■□□□□■■□□□■□□□□■□□□□□■
    □□□■□□□□■□□□□□■□□■□□□□□□□□□□□■■■□□□■□■■□□□□■■□■□□□■□□□■□□■□□□□□□□□□□□■■■□□■■■□■□□□□□□□□□□■□□□■■■□□■□□□□□□■■□□□□■■□□□■□□□□■□□□□□■
    □□□■□□□□■□□□□□■□□■■■■■■□□□□□□□■■■■■■□■■□□□□□■□■□□□□□□□■□□■■■■■■□□□□□□□■■■■■■□□■□□□□□□□□□□■■■■■■□□□■■■■■■□■■□□□□□■□□□■□□□□■□□□□□■
        ''')
    n = int(input(f"{starter}님께서 숫자를 하나 정해주세요: "))
    print("플레이어들은 다른 플레이어 중 한명을 지목하세요!")
    pick = dict()
    for player in players:
        pick[player] = input(f'{player}님의 지목할 상대는?: ')

    pointer = starter

    print('신난다~ 재미난다~ 더 게임 오브 데스!')
    for i in range(n):
        target = pick[pointer]
        print(f'{i+1}: {pointer} -> {target}')
        pointer = target
    print('걸린 사람: ', target)
    return target

# 지하철 술게임
def game03(players, starter):
    # main에서 크롤링한 데이터 가져오기
    global list_subway
    print('-------------------------------------------------------------------------')
    print('경의선: 0   경춘선: 10   수인분당선: 11   공항철도: 12   신분당선: 13')
    print('-------------------------------------------------------------------------')
    try:
        # intro
        subway_num = int(input('지하철~ 지하철! 지하철~ 지하철! 몇호선~ 몇호선? (0~13) 숫자를 입력해주세요 : '))
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
        index_starter = players.index(starter)
        count = count + index_starter
        count = count % len(players)
        # return된 값으로 술마시고 다음 게임을 진행할 사람을 정한다
        # count가 0이면 같은 사람이 다음 게임 시작
        # count가 1이면 리스트에 저장된 순서의 다음 사람이 게임 시작
        return players[count]


class User:
    def __init__(self, name, tolerance, glasses=0):  # 이름과 주량, 마신 잔
        self.name = name
        self.tolerance = tolerance
        self.glasses = glasses

# 남은 주량 보여주는 함수


def display_tolerance():
    for user in users:
        print(f'{user.name}은(는) 지금까지 {user.glasses}! 치사량까지 {user.tolerance}')

# 게임을 실행하는 함수

# 게임 참여자들의 이름을 담은 리스트 리턴 함수


def make_users_name(users):
    users_name = []
    for user in users:
        users_name.append(user.name)
    print(users_name)
    return users_name


def game_start(game_starter, users_names):
    games = ['더게임오브데스', '', '지하철 게임']
    print('오늘의 Alcohol GAME')
    for i, game in enumerate(games):
        print(f'{i+1}. {game}')
    curr_game_index = int(
        input(f'{game_starter}(이)가 좋아하는 랜덤 게임~ 랜덤 게임~ 무슨 게임~? : '))
    if curr_game_index == 1:
        curr_game_loser = game01(users_names, game_starter)
    elif curr_game_index == 3:
        curr_game_loser = game03(users_names, game_starter)
    return curr_game_loser

# 웹크롤링


def crawling():
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
    return list_subway





list_subway = crawling()

while True:
    gameStart = input('게임을 진행할까요? (y/n) :')
    if gameStart == 'n':
        print('게임을 종료합니다.')
        break
    elif gameStart == 'y':
        friends = ['은서', '하연', '연서', '예진', '헌도']
        users = []  # 게임 참여하는 유저 리스트
        tolerance = {1: 2, 2: 4, 3: 6, 4: 8, 5: 10}  # 주량

        user_name = input('오늘 거하게 취해볼 당신의 이름은? : ')

        print("소주 기준 당신의 주량은?")
        print('1. 소주 반병(2잔)')
        print('2. 소주 반병에서 한병 (4잔)')
        print('3. 소주 한병에서 한병 반 (6잔)')
        print('4. 소주 한병 반에서 두병 (8잔)')
        print('5. 소주 두병 이상 (10잔)')

        while True:
            try:
                num_input = int(input('당신의 주량은 얼마만큼인가요? (1~5중 하나를 선택해주세요) : '))
                if not(isinstance(num_input, int)):
                    raise TypeError('정수를 입력해주세요')
                if not(1 <= num_input <= 5):
                    raise ValueError('정수 범위 확인!!!')
                else:
                    break
            except TypeError as e:
                print(e)
            except ValueError as e:
                print(e)
        user_tolerance = tolerance[num_input]

        # 사용자와 주량 users에 추가
        users.append(User(user_name, user_tolerance))
        while True:
            try:
                fnumber = int(
                    input('함께 취할 친구들은 얼마나 필요하신가요? (3명까지 초대할 수 있어요!) : '))
                if not(isinstance(fnumber, int)):
                    raise TypeError('정수를 입력해주세요')
                if not(1 <= fnumber <= 3):
                    raise ValueError('정수 범위 확인!!!')
                else:
                    break
            except TypeError as e:
                print(e)
            except ValueError as e:
                print(e)

        # 친구와 주량 생성 후 users에 추가
        rlist = [0]  # 유저 중복 방지를 위한 리스트
        for i in range(fnumber):
            random_friend_index = random.randint(1, len(friends)-1)
            while random_friend_index in rlist:
                random_friend_index = random.randint(1, len(friends)-1)
            rlist.append(random_friend_index)

            random_tolerance_index = random.randint(1, 5)
            users.append(
                User(friends[random_friend_index], tolerance[random_tolerance_index]))
            print(
                f'오늘 함께 취할 친구는 {friends[random_friend_index]}입니다 ! (치사량 : {tolerance[random_tolerance_index]})')

        i = 0
        game_starter = user_name
        users_names = make_users_name(users)
        while True:
            display_tolerance()
            curr_game_loser = game_start(game_starter, users_names)
            game_starter = curr_game_loser
            for user in users:
                if curr_game_loser == user.name:
                    user.tolerance -= 1
                    user.glasses += 1
                    if user.tolerance == 0:
                        total_game_loser = user.name
                        display_tolerance()
                        print('GAME OVER')
                        print(
                            '~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
                        print(
                            f'{total_game_loser}이(가) 전사했습니다... 꿈나라에서는 편히 쉬시길..zzz')
                        print(
                            '~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
                        print('다음에 술마시면 또 불러주세요~ 안녕!')
                        print(
                            '~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
                        sys.exit(0)
            i += 1

    else:
        print('잘못된 입력입니다.')
