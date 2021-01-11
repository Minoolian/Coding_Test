# 재미있는 오셀로 게임

# 인덱스를 활용한 풀이.
# https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AWQmA4uK8ygDFAXj&categoryId=AWQmA4uK8ygDFAXj&categoryType=CODE

idx_x=[0,1,0,-1,1,-1,1,-1]
idx_y=[1,0,-1,0,1,-1,-1,1]

def play(x, y, dir, col):
    nx=x+idx_x[dir]
    ny=y+idx_y[dir]

    if 0<=nx<n and 0<=ny<n:
        if board[nx][ny]==col:
            return True
        elif board[nx][ny]==None:
            return False
        else:
            if play(nx, ny, dir, col):
                board[nx][ny]=col
                return True
    else:
        return False

t=int(input())

for tc in range(1, t+1):

    n,m=map(int,input().split())
    board=[[None]*n for _ in range(n)]

    board[n//2][n//2]=2
    board[n//2-1][n//2-1]=2
    board[n//2-1][n//2]=1
    board[n//2][n//2-1]=1

    for _ in range(m):
        y, x, col=map(int,input().split())
        board[x-1][y-1]=col
        for i in range(8):
            play(x-1,y-1,i,col)

    w=0; b=0
    for lis in board:
        b+=lis.count(1)
        w+=lis.count(2)

    print("#{} {} {}".format(tc, b, w))