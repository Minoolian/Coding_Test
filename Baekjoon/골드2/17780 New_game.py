# 새로운 게임

# 주어진 로직을 통한 풀이
# https://www.acmicpc.net/problem/17780

# 새로운 체스판을 빈리스트로 만들고 append 와 slice로 옮기기
import sys

dx=[0,0,-1,1]
dy=[1,-1,0,0]

def move(num):
    x,y,dir=mal[num]
    if num!=loc[x][y][0]:
        return 0

    nx=x+dx[dir]
    ny=y+dy[dir]

    if not 0<=nx<N or not 0<=ny<N or chess[nx][ny]==2:
        if dir==0 or dir==1:
            ndir=(dir+1)%2
        else: # 2,3
            ndir=(dir-1)%2+2

        mal[num][2]=ndir
        nx=x+dx[ndir]
        ny=y+dy[ndir]

        if not 0<=nx<N or not 0<=ny<N or chess[nx][ny]==2:
            return 0

    ch=loc[x][y]
    loc[x][y]=[]
    if chess[nx][ny]==1:
        ch=ch[::-1]

    for i in ch:
        loc[nx][ny].append(i)
        mal[i][:2]=[nx,ny]

    if len(loc[nx][ny])>=4:
        return 1

    return 0

N,K=map(int, input().split())
chess=[list(map(int, input().split())) for _ in range(N)]
loc=[[[] for _ in range(N)] for _ in range(N)]
mal=[[] for _ in range(K)]
for i in range(K):
    x,y,dir=map(int,input().split())
    mal[i]=[x-1,y-1,dir-1]
    loc[x-1][y-1].append(i)

cnt=1
while cnt<=1000:
    for i in range(K):
        if move(i):
            print(cnt)
            sys.exit()
    cnt+=1

print(-1)


