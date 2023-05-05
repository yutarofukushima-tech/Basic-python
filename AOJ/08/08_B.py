list = []
while True:
    a = input()
    t = 0
    if a == str(0):
        break
    for x in a:
        t += int(x)
    list.append(t)
for y in list:
    print(y)