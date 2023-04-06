tab=[[[0]*10 for i in range (0,3)]for k in range (0,4)]
N= int(input())
for loop in range(N):
    house,floor,room,add=map(int,input().split())
    tab[house-1][floor-1][room-1]+=add
for i in range(4):
    if i !=0:
        print('#'*20)
    for a in range(3):
        for b in range(10):
            print(' %d'%(tab[i][a][b]),end='')
        print()