class Dice:

    def __init__(self, roll):
        self.a, self.b, self.c, self.d, self.e, self.f = roll 
        
    def direction(self, n):
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

    def check(self, roll):
        for n in 'EEESEEESEEENEEENEEESEEEN':
            if self.result() == roll:
                return True
            self.direction(n)
        else:
            return False

m=int(input())
L=[]
for i in range(m):
    roll = list(map(int, input().split()))
    d = Dice(roll)
    for d in L:
        if d.check(roll):
            break
    else:
        L.append(d)
        continue
    print("No")
    break
else:
    print("Yes")