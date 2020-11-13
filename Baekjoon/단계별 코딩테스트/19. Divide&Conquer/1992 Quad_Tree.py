# 쿼드트리

# 모두 0으로만 되어 있으면 압축 결과는 "0"이 되고, 모두 1로만 되어 있으면 압축 결과는 "1"이 된다.
# 만약 0과 1이 섞여 있으면 전체를 한 번에 나타내지를 못하고, 왼쪽 위, 오른쪽 위, 왼쪽 아래, 오른쪽 아래, 이렇게 4개의 영상으로 나누어 압축하게 되며,
# 이 4개의 영역을 압축한 결과를 차례대로 괄호 안에 묶어서 표현

# 색종이 문제와 거의 흡사

import sys

def division(x,y,n):

    color=paper[x][y]
    for i in range(x,x+n):
        for j in range(y,y+n):
            if color!=paper[i][j]:
                print("(", end="")
                division(x,y,n//2) # 1사분면
                division(x,y+n//2,n//2) # 2사분면
                division(x+n//2,y,n//2) # 3사분면
                division(x+n//2,y+n//2,n//2) # 4사분면
                print(")", end="")
                return

    if color=="1":
        print("1",end="")
    else:
        print("0",end="")

n=int(sys.stdin.readline())
paper=[sys.stdin.readline().rstrip() for _ in range(n)]
division(0,0,n)
