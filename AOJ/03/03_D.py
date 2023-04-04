a,b,c=map(int,input().split())
t=0
for x in range(a,b+1):
    if c%x==0:
        t+=1
print(t)