a,b,c = map(int,input().split())
def min(a,b,c):
    if a<=b and a<=c:
        return a
    else:
        if b<=c:
            return b
        else:
            return c
def max(a,b,c):
    if a>=b and a>=c:
        return a
    else:
        if b>=c:
            return b
        else:
            return c
def mid(a,b,c):
    if min(a,b,c)<a<max(a,b,c):
        return a
    else:
        if min(a,b,c)<b<max(a,b,c):
            return b
        else:
            return c

d=min(a,b,c)
e=mid(a,b,c)
f=max(a,b,c)
print(d, e, f)