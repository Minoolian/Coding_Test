# 유기농 배추

# 배추를 군데군데 심어놓았다.
# 배추들이 모여있는 곳에는 배추흰지렁이가 한 마리만 있으면 되므로 서로 인접해있는 배추들이 몇 군데에 퍼져있는지 조사하면 총 몇 마리의 지렁이가 필요한지 알 수 있다.

# 앞선 단지번호 붙이기 문제와 매우 유사하다.

import sys
from collections import deque

vec_x = [-1, 0, 1, 0] # 상하좌우를 이동할 vector
vec_y = [0, 1, 0, -1]

def bfs(x, y): # 단지번호 붙이기는 DFS로 해당 문제는 BFS로 구현했다.
    q.append([x,y])
    visit[x][y]=1

    while q:
        a,b=q.popleft()

        for i in range(4):
            nx=a+vec_x[i]
            ny=b+vec_y[i]
            if nx<0 or nx>=m or ny<0 or ny>=n:
                continue

            if visit[nx][ny]==0 and [nx,ny] in lis:
                q.append([nx,ny])
                visit[nx][ny]=1

t = int(sys.stdin.readline())

for _ in range(t):
    m, n, k = map(int, sys.stdin.readline().split())
    lis = [list(map(int, sys.stdin.readline().split())) for _ in range(k)]
    visit = [[0] * n for _ in range(m)]
    q=deque()
    count=0

    for i in range(m):
        for j in range(n):
            if visit[i][j]==0 and [i,j] in lis:
                bfs(i, j)
                count+=1
    print(count)

