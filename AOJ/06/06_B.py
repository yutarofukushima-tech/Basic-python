suit='SHCD'
n=int(input())
exist=[[False]*14 for i in range(4)]
for i in range(n):
    b,num = input().split()
    num=int(num)
    exist[suit.find(b)][num]=True
for i in range(4):
    for j in range(1,14):
        if not exist[i][j]:
            print(suit[i], j)