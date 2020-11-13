# 줄세우기

# 일부 학생들의 키를 비교한 결과가 주어졌을 때, 줄을 세우는 프로그램을 작성
# 첫째 줄에 N, M이 주어진다. M은 키를 비교한 횟수
# 다음 M개의 줄에는 키를 비교한 두 학생의 번호 A, B가 주어진다. 이는 학생 A가 학생 B의 앞에 서야 한다는 의미이다.

import sys
from collections import deque
input=sys.stdin.readline

n,m=map(int,input().split())
temp=[list(map(int, input().split())) for _ in range(m)]
indegree=[0 for _ in range(32001)]
# indegree는 특정노드 탐색 이전에 먼저 탐색되어야 하는 노드의 수를 저장.
g=[[] for _ in range(32001)]
q=deque()

for a,b in temp:
    indegree[b]+=1
    g[a].append(b)

for i in range(1, n+1):
# 초기 모든 정점에 대해 들어오는 간선이 없는 정점을 q에 삽입(indegree로 확인)
    if indegree[i]==0:
        q.append(i)

while q:
    h=q.popleft()

    for i in g[h]:
        indegree[i]-=1
        # 간선 삭제
        if indegree[i]==0:
        # 추가로 발견되는 들어오는 간선이 없는 정점을 q에 삽입
            q.append(i)
    print(h, end=" ")