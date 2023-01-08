import random
import sys
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
        while True:
            targetOfPlayer = input(f'{player}님의 지목할 상대는?: ')
            if targetOfPlayer not in players:
                print('게임을 플레이하고 있는 유저 중에서 지목해주세요!')
            else:
                pick[player] = targetOfPlayer
                break
    pointer = starter

    print('신난다~ 재미난다~ 더 게임 오브 데스!')
    for i in range(n):
        target = pick[pointer]
        print(f'{i+1}: {pointer} -> {target}')
        pointer = target
    print('걸린 사람: ', target)
    return target


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
    games = ['더게임오브데스']
    print('오늘의 Alcohol GAME')
    for i, game in enumerate(games):
        print(f'{i+1}. {game}')
    curr_game_index = int(
        input(f'{game_starter}(이)가 좋아하는 랜덤 게임~ 랜덤 게임~ 무슨 게임~? : '))
    if curr_game_index == 1:
        curr_game_loser = game01(users_names, game_starter)
    return curr_game_loser


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
