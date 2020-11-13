# 벽 부수고 이동하기

# (1, 1)에서 (N, M)의 위치까지 이동
# 도중에 한 개의 벽을 부수고 이동하는 것이 좀 더 경로가 짧아진다면, 벽을 한 개 까지 부수고 이동

import sys
from collections import deque

dx=[1,-1,0,0]
dy=[0,0,1,-1]

def bfs():
    q=deque([[1,0,0]])
    visit[1][0][0]=1

    while q:
        z,x,y=q.popleft()

        if x== n-1 and y == m-1:
            return visit[z][x][y]

        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]

            if 0<=nx<n and 0<=ny<m:
                if lis[nx][ny]==1 and z==1:
                # 벽이 막고있는데, 벽을 부술 수 있다면.
                    visit[0][nx][ny] = visit[1][x][y]+1
                    q.append([0,nx,ny])
                elif lis[nx][ny]==0 and visit[z][nx][ny]==0:
                # 이동할 수 있고, 한번도 방문하지 않았다면.
                    visit[z][nx][ny] = visit[z][x][y]+1
                    q.append([z,nx,ny])
    return -1

n,m=map(int,sys.stdin.readline().split())
lis=[list(map(int,list(sys.stdin.readline().strip()))) for _ in range(n)]
visit=[[[0]*m for _ in range(n)] for i in range(2)]
# 3차원 리스트의 z값을 벽을 부순 여부로 나타낸다.

print(bfs())