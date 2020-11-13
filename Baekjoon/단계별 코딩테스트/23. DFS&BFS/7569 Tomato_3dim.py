# 토마토

# 익은 토마토들의 인접한 곳에 있는 익지 않은 토마토들은 익은 토마토의 영향을 받아 익게 된다.
# 토마토가 모두 익을 때까지의 최소 날짜를 출력해야 한다. 만약, 저장될 때부터 모든 토마토가 익어있는 상태이면 0을 출력해야 하고, 토마토가 모두 익지는 못하는 상황이면 -1을 출력

import sys
from collections import deque

vec_x = [-1, 0, 1, 0, 0, 0] # 위, 아래, 왼쪽, 오른쪽, 앞, 뒤를 이동할 vector
vec_y = [0, 1, 0, -1, 0, 0]
vec_z = [0, 0, 0, 0, 1, -1]

m,n,h=map(int,sys.stdin.readline().split())
lis=[[list(map(int,sys.stdin.readline().split())) for _ in range(n)] for _ in range(h)]
day=-1

def bfs():
    global day

    while q:
        day+=1

        for _ in range(len(q)): # 익은 토마들의 주변 토마토들을 익힌다.
            c,a,b=q.popleft()

            for i in range(6):
                x=a+vec_x[i]
                y=b+vec_y[i]
                z=c+vec_z[i]

                if x < 0 or x >= n or y < 0 or y >= m or z<0 or z>=h:
                    continue

                if lis[z][x][y]==0:
                    q.append([z, x, y])
                    lis[z][x][y]=1

    for a in lis: # 탐색이 끝나고 안익은 토마토가 하나라도 존재하면
        for b in a:
            if 0 in b:
                return -1
    return day

q=deque()

for k in range(h):
    for i in range(n):
        for j in range(m): # 3차원 리스트의 z원소는 맨 앞으로 배치한다.
            if lis[k][i][j]==1: # 동시에 익을 것이기 때문에 익은 토마토들을 먼저 담는다.
                q.append([k,i,j])
print(bfs())



