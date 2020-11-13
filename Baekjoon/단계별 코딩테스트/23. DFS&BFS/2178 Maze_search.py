# 미로 탐색

# 미로가 주어졌을 때, (1, 1)에서 출발하여 (N, M)의 위치로 이동할 때 지나야 하는 최소의 칸 수를 구하는 프로그램

import sys
from collections import deque

vec_x = [-1, 0, 1, 0] # 상하좌우를 이동할 vector
vec_y = [0, 1, 0, -1]

n,m=map(int,sys.stdin.readline().split())
lis=[sys.stdin.readline().rstrip() for _ in range(n)]
visit=[[0]*m for _ in range(n)]


def bfs():
    # BFS는 각 정점을 최단경로로 방문한다는 특징이 있다.
    visit[0][0]=1
    q=deque([[0,0]])

    while q:
        a,b=q.popleft()

        for i in range(4):
            x=a+vec_x[i]
            y=b+vec_y[i]

            if x < 0 or x >= n or y < 0 or y >= m:
                continue

            if visit[x][y] == 0 and lis[x][y]=='1':
                q.append([x, y])
                visit[x][y] = visit[a][b]+1
                # 이전 예제들과 달리 방문 여부를 1씩 증가시키면
                # 방문 순서가 되므로 거리를 구할 수 있다.

bfs()
print(visit[n-1][m-1])