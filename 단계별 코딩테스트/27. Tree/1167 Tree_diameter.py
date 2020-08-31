# 트리의 지름

# 첫 번째 줄에서는 트리의 정점의 개수 V가 주어지고, 둘째 줄부터 V개의 줄에 걸쳐 간선의 정보가 주어진다.
# 예를 들어 정점 3은 정점 1과 거리가 2인 간선으로 연결되어 있고, 정점 4와는 거리가 3인 간선으로 연결되어 있는 것을 보여준다. 각 줄의 마지막에는 -1이 입력으로 주어진다.
# 트리의 지름을 출력한다.

# 1967 트리의 지름 문제와 입력의 차이만 존재한다.
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

for i in range(n):
    check=list(map(int, sys.stdin.readline().split()))
    if check[3]==-1:
        lis[check[0]-1].append([check[2],check[1]-1])
        lis[check[1]-1].append([check[2],check[0]-1])
    else:
        lis[check[0]-1].append([check[2],check[1]-1])
        lis[check[1]-1].append([check[2],check[0]-1])
        lis[check[0]-1].append([check[4],check[3]-1])
        lis[check[3]-1].append([check[4],check[0]-1])

print(bfs(bfs(0,1), 2))