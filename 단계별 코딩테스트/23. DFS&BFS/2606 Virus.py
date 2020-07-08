# 바이러스

# 1번 컴퓨터를 통해 웜 바이러스에 걸리게 되는 컴퓨터의 수를 출력하는 프로그램

import sys
from collections import deque

n=int(sys.stdin.readline())
m=int(sys.stdin.readline())
visit=[0 for _ in range(n+1)]
s=[[0]*(n+1) for _ in range(n+1)]

for i in range(m):
    x, y=map(int, sys.stdin.readline().split())
    s[x][y], s[y][x]=1, 1

def dfs(v): # DFS는 재귀함수로 구현
    global count
    visit[v]=1
    for i in range(1, n+1):
        if visit[i]==0 and s[v][i]==1:
            count += 1 # 1번 PC를 제외한 감연된 PC 수 카운트
            dfs(i)

def bfs(v): # BFS는 queue 로 구현
    global count
    queue=deque([v])
    visit[v]=1

    while queue:
        v=queue.popleft()

        for i in range(1, n+1):
            if visit[i]==0 and s[v][i]==1:
                visit[i] = 1
                count += 1 # 1번 PC를 제외한 감염된 PC수 카운트
                queue.append(i)

# 기존 DFS, BFS 의 시작노드를 1로 한후 실행하면 성공
count=0
# dfs(1)
bfs(1)
print(count)



