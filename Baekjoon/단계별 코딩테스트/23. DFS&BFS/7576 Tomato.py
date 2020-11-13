# 토마토

# 익은 토마토들의 인접한 곳에 있는 익지 않은 토마토들은 익은 토마토의 영향을 받아 익게 된다.
# 토마토가 모두 익을 때까지의 최소 날짜를 출력해야 한다. 만약, 저장될 때부터 모든 토마토가 익어있는 상태이면 0을 출력해야 하고, 토마토가 모두 익지는 못하는 상황이면 -1을 출력

import sys
from collections import deque

vec_x = [-1, 0, 1, 0] # 상하좌우를 이동할 vector
vec_y = [0, 1, 0, -1]

m,n=map(int,sys.stdin.readline().split())
lis=[list(map(int,sys.stdin.readline().split())) for _ in range(n)]
visit=[[0]*m for _ in range(n)]
day=-1

def bfs():
    global day

    while q:
        day+=1

        for _ in range(len(q)): # 익은 토마들의 주변 토마토들을 익힌다.
            a,b=q.popleft()

            for i in range(4):
                x=a+vec_x[i]
                y=b+vec_y[i]

                if x < 0 or x >= n or y < 0 or y >= m:
                    continue

                if lis[x][y]==0:
                    q.append([x, y])
                    lis[x][y]=1

    for a in lis: # 탐색이 끝나고 안익은 토마토가 하나라도 존재하면
        if 0 in a:
            return -1
    return day

q=deque()

for i in range(n):
    for j in range(m):
        if lis[i][j]==1: # 동시에 익을 것이기 때문에 익은 토마토들을 먼저 담는다.
            q.append([i,j])
print(bfs())



