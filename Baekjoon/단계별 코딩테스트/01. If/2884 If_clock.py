a,b=map(int,input().split())

if b-45>=0:
    b=b-45
else:
    if a-1>=0:
        a=a-1       
    else:
        a=23
    b=b+15

print(a,b)