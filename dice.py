import random


class Dice:
    def __init__(self, name, val = 6):
        self.face_num = val
        self.nickname = name

    def shoot(self):
        p = random.randint(1, self.face_num)
        return p



class Odd_or_Even(Dice):
    def display(self):
        return self.shoot()


    def OddorEven(self):
        p = self.display()

        if p % 2 == 0:
            r = "Even"
        else:
            r = "Odd"

        print(self.nickname, p, r)


OEList = []
s = len(OEList)-1

for i in range(4):
    newdice_a = Odd_or_Even("dice" + str(1)).OddorEven()

    OEList.append(newdice_a)

if OEList[s] == "Odd":
    print("奇数：サイコロの色は白")
else:
    print("偶数：サイコロの色は赤")