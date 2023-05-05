class Dice:

    def __init__(self, roll):
        self.a, self.b, self.c, self.d, self.e, self.f = roll 
        
    def direction(self, op):
        if n == "N":
            self.a, self.e, self.f, self.b \
                = self.b, self.a, self.e, self.f
        elif n == "S":
            self.a, self.e, self.f, self.b \
                = self.e, self.f, self.b, self.a
        elif n == "W":
            self.a, self.d, self.f, self.c \
                = self.c, self.a, self.d, self.f
        elif n == "E":
            self.a, self.d, self.f, self.c \
                = self.d, self.f, self.c, self.a

    def result(self):
        return [self.a, self.b, self.c, self.d, self.e, self.f]

roll = list(map(int, input().split()))
dice_6 = Dice(roll)
roll2= list(map(int, input().split()))
for n in 'EEESEEESEEENEEENEEESEEEN':
    if dice_6.result() == roll2:
        print("Yes")
        break
    else:
        dice_6.direction(n)
else:
    print("No")