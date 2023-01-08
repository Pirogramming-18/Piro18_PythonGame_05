player__list = ['유진','서영','형준','혁수'] # 임의로 생성 
name = '유진' # 임의로 생성 
profile = [['유진', 4, 0], ['서영', 4, 0], ['형준', 4, 0], ['혁수', 4, 0]] # 임의로 생성 ['이름', 주량, 마신 잔 수]

def start369(profile, name):
    import random
    import copy

    print("""
 ____    _    __  ____   ___   _ _  ______ _   _    ____    _    __  __ _____ 
/ ___|  / \  |  \/  \ \ / / | | | |/ / ___| | | |  / ___|  / \  |  \/  | ____|
\___ \ / _ \ | |\/| |\ V /| | | | ' / |  _| | | | | |  _  / _ \ | |\/| |  _|  
 ___) / ___ \| |  | | | | | |_| | . \ |_| | |_| | | |_| |/ ___ \| |  | | |___ 
|____/_/   \_\_|  |_| |_|  \___/|_|\_\____|\___/   \____/_/   \_\_|  |_|_____|\n""")

    # 게임 시작 값
    num = 1

    # 첫 순서 랜덤으로 정하기
    default = copy.deepcopy(profile) # 셔플 되기 전
    random.shuffle(default)
    print(default)
    player = 0

    # 369 게임
    while True:
        player__list = default[player][0]
        if player__list == name: # 내 차례
            turn = input('숫자를 입력하세요: ')
            if num % 3 > 0: # 숫자가 3의 배수가 아닐 때
                try:
                    int(turn)
                except ValueError:
                    print("땡!")
                    break
                else:
                    if int(turn) != num:
                        print("땡!")
                        break

                    else: # 정답
                        num += 1
                        player += 1
                       
                        player %= len(default)  # 플레이어 수만큼 나누기
                        continue

            elif num % 3 == 0: # 숫자가 3의 배수일 때
                if turn != '짝':
                    print('땡!')
                    break

                elif turn == '짝': # 정답
                    num += 1
                    player += 1
                    player %= len(default) # 플레이어 수만큼 나누기
                    continue

        else: # 컴퓨터 차례
            answer__list = [num, '짝']
            turn = random.choice(answer__list) # 답 랜덤 선택
            if num % 3 > 0: # 숫자가 3의 배수가 아닐 때
                try:
                    int(turn)
                except ValueError: 
                    print(player__list, ":", turn)
                    print("땡!")
                    break
                else: # 정답
                    print(player__list, ":", turn)
                    num += 1
                    player += 1
                    player %= len(default)  # 플레이어 수만큼 나누기
                    continue

            elif num % 3 == 0: # 숫자가 3의 배수일 때
                if turn != '짝':
                    print(player__list, ":", turn)
                    print('땡!')
                    break

                elif turn == '짝': # 정답
                    print(player__list, ":", turn)
                    num += 1
                    player += 1
                    player %= len(default) # 플레이어 수만큼 나누기
                    continue

    # 마지막에 답변한 player가 벌칙 수행
    profile[profile.index(default[player])][2] += 1
    print(player__list+'님이 졌습니다. 술이 들어간다 쭉쭉쭉 쭉쭉! 쭉쭉쭉 쭉쭉!')

start369(profile, name)