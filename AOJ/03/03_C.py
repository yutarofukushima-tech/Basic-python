t=1
while True:
    a,b = map(int,input().split())
    if a==0 and b==0:
        break
    else:
        if a>b:
            a,b = b,a
        print(a, b)
        t=t+1