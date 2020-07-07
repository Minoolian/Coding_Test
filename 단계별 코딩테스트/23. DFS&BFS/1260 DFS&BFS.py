# DFS와 BFS

# 그래프를 DFS로 탐색한 결과와 BFS로 탐색한 결과를 출력하는 프로그램

import sys
from collections import deque

n,m,v=map(int,sys.stdin.readline().split())
visit=[0 for _ in range(n+1)]
s=[[0]*(n+1) for _ in range(n+1)]

for i in range(m):
    x, y=map(int, sys.stdin.readline().split())
    s[x][y], s[y][x]=1, 1

def dfs(v): # DFS는 재귀함수로 구현
    print(v, end=' ')
    visit[v]=1
    for i in range(1, n+1):
        if visit[i]==0 and s[v][i]==1:
            dfs(i)

def bfs(v): # BFS는 queue 로 구현
    queue=deque([v])
    visit[v]=0 # DFS 결과를 초기화(visit)

    while queue:
        v=queue.popleft()
        print(v, end=' ')
        for i in range(1, n+1):
            if visit[i]==1 and s[v][i]==1:
                queue.append(i)
                visit[i]=0

dfs(v)
print()
bfs(v)


