while True:
    a,op,b=input().split()
    x=0
    a,b=int(a), int(b)
    if op == '?':
        break
    if op == '+':
        x=a+b
    if op == '-':
        x=a-b
    if op == '*':
        x=a*b
    if op == '/':
        x=a//b
    print(x,end='\n')