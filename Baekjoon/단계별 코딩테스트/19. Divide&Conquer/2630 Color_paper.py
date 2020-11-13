# 색종이 만들기

# 모두 하얀색 또는 모두 파란색으로 칠해져 있거나, 하나의 정사각형 칸이 되어 더 이상 자를 수 없을 때까지 반복

import sys

white=0 ; blue=0

def division(x,y,n):
    global white,blue

    color=paper[x][y]
    for i in range(x,x+n):
        for j in range(y,y+n):
            if color!=paper[i][j]:
                division(x,y,n//2) # 1사분면
                division(x,y+n//2,n//2) # 2사분면
                division(x+n//2,y,n//2) # 3사분면
                division(x+n//2,y+n//2,n//2) # 4사분면
                return

    if color==1:
        blue+=1
    else:
        white+=1

n=int(sys.stdin.readline())
paper=[list(map(int,sys.stdin.readline().split())) for _ in range(n)]
division(0,0,n)
print(white,blue,sep='\n')
