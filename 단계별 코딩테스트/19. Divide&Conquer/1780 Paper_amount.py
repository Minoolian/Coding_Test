# 종이의 개수

# 1. 만약 종이가 모두 같은 수로 되어 있다면 이 종이를 그대로 사용한다.
# 2. (1)이 아닌 경우에는 종이를 같은 크기의 9개의 종이로 자르고, 각각의 잘린 종이에 대해서 (1)의 과정을 반복한다.

import sys

minus_one=0; zero=0; one=0

def division(x,y,n):
    global minus_one,one,zero

    color=paper[x][y]
    for i in range(x,x+n):
        for j in range(y,y+n):
            if color!=paper[i][j]: # 종이위에 하나라도 같지 않은것이 있다면,
                for i in range(3): # 9분할하여 다시 수행
                    for j in range(3):
                        division(x + i * (n // 3), y + j * (n // 3), n // 3)
                return


    if color == -1:
        minus_one += 1
    elif color == 0:
        zero += 1
    else:
        one += 1
    return



n=int(sys.stdin.readline())
paper=[list(map(int,sys.stdin.readline().split())) for _ in range(n)]
division(0,0,n)
print(minus_one,zero,one,sep='\n')