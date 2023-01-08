import random

class User:
    def __init__(self, name, tolerance, glasses=0):  # 이름과 주량, 마신 잔
        self.name = name
        self.tolerance = tolerance
        self.glasses = glasses

curr_player = 0
users = [User('유진', 4, 0), User('서영', 4, 0), User('형준', 4, 0), User('혁수', 4, 0)]

def game02(curr_player, users):
    print("""
 ____    _    __  ____   ___   _ _  ______ _   _    ____    _    __  __ _____ 
/ ___|  / \  |  \/  \ \ / / | | | |/ / ___| | | |  / ___|  / \  |  \/  | ____|
\___ \ / _ \ | |\/| |\ V /| | | | ' / |  _| | | | | |  _  / _ \ | |\/| |  _|  
 ___) / ___ \| |  | | | | | |_| | . \ |_| | |_| | | |_| |/ ___ \| |  | | |___ 
|____/_/   \_\_|  |_| |_|  \___/|_|\_\____|\___/   \____/_/   \_\_|  |_|_____|\n""")
    
    order_num = curr_player
    number = 1
    p = [True, True, True, True, False]
    
    while True:
        if order_num >= len(users):
            order_num = 0
        
        if order_num == 0:
            correct = ""
            if number//10==3 or number//10==6 or number//10==9:
                correct += "짝"
            if number%10==3 or number%10==6 or number%10==9:
                correct += "짝"
            if correct == "":
                correct += str(number)
            answer = input(users[order_num].name + " 님 : ")
            if answer != correct:
                print("땡!")
                print("당신이 졌습니다. 술이 들어간다 쭉쭉쭉 쭉쭉! 쭉쭉쭉 쭉쭉!\n")
                users[order_num].glasses += 1
                break    
        else:
        
            correct = ""
            print(users[order_num].name, "님 : ", end='')
            if number//10==3 or number//10==6 or number//10==9:
                correct += "짝"
            if number%10==3 or number%10==6 or number%10==9:
                correct += "짝"
            if correct == "":
                correct += str(number)

            answer = ""
            if number//10==3 or number//10==6 or number//10==9:
                x = random.randint(0, 4)
                if p[x]: 
                    answer += "짝"
            if number%10==3 or number%10==6 or number%10==9:
                x = random.randint(0, 4)
                if p[x]: 
                    answer += "짝"
            if answer == "":
                answer += str(number)
            print(answer)

            if answer != correct:
                print("땡!")
                print(users[order_num].name, "님이 졌습니다. 술이 들어간다 쭉쭉쭉 쭉쭉! 쭉쭉쭉 쭉쭉!\n")
                users[order_num].glasses += 1
                break

        print("\n")
        order_num += 1
        number += 1

game02(curr_player, users)
