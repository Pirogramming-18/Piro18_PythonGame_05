# 공산당 게임
class TargetError(Exception):
    def __init__(self):
        super().__init__('이름이 틀린 것 같소.. 다시 입력하시라요!\n')

class OrderError(Exception):
    def __init__(self):
        super().__init__('명령은 0과 1뿐.. 다시 입력하시라요!\n')

def printEndMsg(loser):
    print(f'\n누가 술을 마셔~ {loser}(이)가 술을 마셔🍺 \n{loser[0]}👏👏 👏👏 {loser[1]}👏👏 👏👏 원~~샷!\n')

def game04(players,starter):

    # 게임 시작 ascii art 출력
    #printLine()
    print("""
░██████╗░░█████╗░███╗░░██╗░██████╗░░██████╗░█████╗░███╗░░██╗
██╔════╝░██╔══██╗████╗░██║██╔════╝░██╔════╝██╔══██╗████╗░██║
██║░░██╗░██║░░██║██╔██╗██║██║░░██╗░╚█████╗░███████║██╔██╗██║
██║░░╚██╗██║░░██║██║╚████║██║░░╚██╗░╚═══██╗██╔══██║██║╚████║
╚██████╔╝╚█████╔╝██║░╚███║╚██████╔╝██████╔╝██║░░██║██║░╚███║
░╚═════╝░░╚════╝░╚═╝░░╚══╝░╚═════╝░╚═════╝░╚═╝░░╚═╝╚═╝░░╚══╝

██████╗░░█████╗░███╗░░██╗░██████╗░░░░░░░░██████╗░░█████╗░███╗░░░███╗███████╗
██╔══██╗██╔══██╗████╗░██║██╔════╝░░░░░░░██╔════╝░██╔══██╗████╗░████║██╔════╝
██║░░██║███████║██╔██╗██║██║░░██╗░█████╗██║░░██╗░███████║██╔████╔██║█████╗░░
██║░░██║██╔══██║██║╚████║██║░░╚██╗╚════╝██║░░╚██╗██╔══██║██║╚██╔╝██║██╔══╝░░
██████╔╝██║░░██║██║░╚███║╚██████╔╝░░░░░░╚██████╔╝██║░░██║██║░╚═╝░██║███████╗
╚═════╝░╚═╝░░╚═╝╚═╝░░╚══╝░╚═════╝░░░░░░░░╚═════╝░╚═╝░░╚═╝╚═╝░░░░░╚═╝╚══════╝""")
    #printLine()

    #인트로 출력
    print('\n🎶공~산당 공산당 공~산당 공산당!🎶\n')
    starter='유진' #main전이라 임의로 설정해둠
    #게임 진행
    while True:
        try:
            gsdTarget=input(f'\n{starter}님🙌 누구를 지목하시겠습니까?: ')
            if gsdTarget not in players:
                raise TargetError
        except TargetError as e:
            print(e)
            continue
        else:
            while True:
                try:
                    gsdOrder=int(input('\n0: \'동무~😊\' 1: \'마시라우!☠️\' \n과연.. 당신의 선택은?: '))

                    if gsdOrder ==0:
                        starter=players[players.index(gsdTarget)]
                        break
                    elif gsdOrder==1:
                        loser=players[players.index(gsdTarget)]
                        printEndMsg(loser)
                        return loser
                    else:
                        raise OrderError
                except OrderError as e:
                    print(e)