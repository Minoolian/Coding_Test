# 트리의 지름

# 첫 번째 정수는 간선이 연결하는 두 노드 중 부모 노드의 번호를 나타내고, 두 번째 정수는 자식 노드를, 세 번째 정수는 간선의 가중치
# 간선에 대한 정보는 부모 노드의 번호가 작은 것이 먼저 입력되고, 부모 노드의 번호가 같으면 자식 노드의 번호가 작은 것이 먼저 입력
# 트리의 지름을 출력한다.

import sys
from collections import deque

def bfs(x, mode):
    q=deque()
    q.append(x)

    c=[-1 for _ in range(n)]
    c[x]=0

    while q:
        x=q.popleft()
        for w, nx in lis[x]:
            if c[nx] == -1:
                c[nx] = c[x]+w
                q.append(nx)
    if mode == 1:
        return c.index(max(c))
    else:
        return max(c)

n=int(sys.stdin.readline())
lis=[[] for _ in range(n)]

for i in range(n-1):
    x,y,w=map(int, sys.stdin.readline().split())
    lis[x-1].append([w, y-1])
    lis[y-1].append([w, x-1])

print(bfs(bfs(0,1), 2))