x,y,w,h=map(int,input().split())

if h-y>y-0:
    G_1=y-0
else:
    G_1=h-y

if w-x>x-0:
    G_2=x-0
else:
    G_2=w-x

if G_1>G_2:
    print(G_2)
else:
    print(G_1)

# https://hwiyong.tistory.com/222
# x, y, w, h = list(map(int, input().split()))
# print(min([x, y, w - x, h - y])) # 대각선이 최소인 경우는 없다.