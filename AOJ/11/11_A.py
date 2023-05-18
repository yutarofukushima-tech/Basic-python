class Dice:

    def __init__(self):
        self.nu = [i for i in range(0, 6)]
        
    def direction(self):
        if n == "N":
            self.nu[0], self.nu[4], self.nu[5], self.nu[1] \
                = self.nu[1], self.nu[0], self.nu[4], self.nu[5]
        elif n == "S":
            self.nu[0], self.nu[4], self.nu[5], self.nu[1] \
                = self.nu[4], self.nu[5], self.nu[1], self.nu[0]
        elif n == "W":
            self.nu[0], self.nu[3], self.nu[5], self.nu[2] \
                = self.nu[2], self.nu[0], self.nu[3], self.nu[5]
        elif n == "E":
            self.nu[0], self.nu[3], self.nu[5], self.nu[2] \
                = self.nu[3], self.nu[5], self.nu[2], self.nu[0]

    def result(self):
        return self.nu[0]

Dice_list = input().split()
roll = input()
Dice6 = Dice()
for n in roll:
    Dice6.direction()

print(Dice_list[Dice6.result()])