while True:
    n, x = map(int,input().split())
    if n == x == 0:
        break
    t = 0
    for a in range(1,n+1):
        for b in range(1,a):
            for c in range(1,b):
                if a + b + c == x:
                    t+=1
    print(t)