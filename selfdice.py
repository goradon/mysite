class Dice:
    def __init__(self,T,B,U,D,L,R):
        self.dice = [T,B,U,D,L,R]
        self.count = 0

    def search(self,num):
        for i, dice_num in enumerate(self.dice):
            if num == dice_num:
                if i == 1:
                    self.up()
                    self.up()
                elif i == 2:
                    self.up()
                elif i == 3:
                    self.down()
                elif i == 4:
                    self.right()
                elif i == 5:
                    self.left()


    def left(self):
        self.dice[0], self.dice[1], self.dice[5], self.dice[4]= self.dice[5],self.dice[4], self.dice[1],self.dice[0]
        self.count += 1

    def right(self):
        self.dice[1],self.dice[5], self.dice[4],self.dice[0] = self.dice[5], self.dice[0], self.dice[1], self.dice[4]
        self.count += 1

    def down(self):
        self.dice[2],self.dice[1], self.dice[3], self.dice[0] = self.dice[0], self.dice[2], self.dice[1], self.dice[3]
        self.count += 1

    def up(self):
        self.dice[0], self.dice[2], self.dice[1], self.dice[3] = self.dice[2],self.dice[1], self.dice[3], self.dice[0]
        self.count += 1

    def print_dice(self):
        print(self.count)


T,B,U,D,L,R= map(int,input().split())
N = int(input())
d = Dice(T,B,U,D,L,R)
for i in range(N):
    num = int(input())
    d.search(num)
d.print_dice()
