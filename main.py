import random
import sys
from theGameOfDeath import theGameOfDeath

# 게임에 참여하는 유저 클래스


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


def game_start(game_starter):
    games = ['더게임오브데스']
    print('오늘의 Alcohol GAME')
    for i, game in enumerate(games):
        print(f'{i+1}. {game}')
    curr_game_index = int(
        input(f'{game_starter}(이)가 좋아하는 랜덤 게임~ 랜덤 게임~ 무슨 게임~? : '))
    if curr_game_index == 1:
        theGameOfDeath(users, game_starter)


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

        user_tolerance = tolerance[int(input(
            '당신의 주량은 얼마만큼인가요? (1~5중 하나를 선택해주세요) : '))]

        # 사용자와 주량 users에 추가
        users.append(User(user_name, user_tolerance))

        fnumber = int(input('함께 취할 친구들은 얼마나 필요하신가요? (3명까지 초대할 수 있어요!) : '))

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
        while True:
            display_tolerance()
            curr_game_loser = game_start(game_starter)
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
