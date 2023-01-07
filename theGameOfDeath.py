players = ['유진', '서영', '형준', '혁수']
starter = '혁수'


def theGameOfDeath(players, starter):
    n = int(input(f"{starter}님께서 숫자를 하나 정해주세요: "))
    print("플레이어들은 다른 플레이어 중 한명을 지목하세요!")
    pick = dict()
    for player in players:
        pick[player] = input(f'{player}님의 지목할 상대는?: ')

    pointer = starter
    for i in range(n):
        target = pick[pointer]
        print(f'{i+1}: {pointer} -> {target}')
        pointer = target
    print('걸린 사람: ', target)


theGameOfDeath(players, starter)
