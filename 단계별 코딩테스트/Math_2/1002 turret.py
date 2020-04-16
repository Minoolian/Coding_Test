for _ in range(int(input())):
    x_1,y_1,r_1,x_2,y_2,r_2=map(int,input().split())
    d=((x_2-x_1)**2+(y_2-y_1)**2)**0.5
    plus_r=r_1+r_2
    minus_r=abs(r_1-r_2)

    if d==0:
        if r_1==r_2:
            print(-1)
        else:
            print(0)
    elif d==plus_r or d==minus_r:
        print(1)
    elif d<plus_r and d>minus_r:
        print(2)
    else:
        print(0)
