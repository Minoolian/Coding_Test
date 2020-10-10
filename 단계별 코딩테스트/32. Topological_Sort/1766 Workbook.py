# 문제집

# 1. N개의 문제는 모두 풀어야 한다.
# 2. 먼저 푸는 것이 좋은 문제가 있는 문제는, 먼저 푸는 것이 좋은 문제를 반드시 먼저 풀어야 한다.
# 3. 가능하면 쉬운 문제부터 풀어야 한다.

# 첫째 줄에 문제의 수 N과 먼저 푸는 것이 좋은 문제에 대한 정보의 개수 M
# 둘째 줄부터 M개의 줄에 걸쳐 두 정수의 순서쌍 A,B가 빈칸을 사이에 두고 주어진다. 이는 A번 문제는 B번 문제보다 먼저 푸는 것이 좋다는 의미

import sys
import heapq as hq
input=sys.stdin.readline

n,m=map(int,input().split())
g=[[] for _ in range(n+1)]
indegree=[0 for _ in range(32001)]

q=[]

for _ in range(m):
    a,b=map(int,input().split())
    indegree[b]+=1
    g[a].append(b)

for i in range(1, n+1):
# 초기 모든 정점에 대해 들어오는 간선이 없는 정점을 q에 삽입(indegree로 확인)
    if indegree[i]==0:
        hq.heappush(q,i) # 최소힙을 이용해서 쉬운 문제부터 출력

result=[]
while q:
    h=hq.heappop(q)
    result.append(h)
    
    for i in g[h]:
        indegree[i]-=1
        # 간선 삭제
        if indegree[i]==0:
        # 추가로 발견되는 들어오는 간선이 없는 정점을 q에 삽입
            hq.heappush(q,i)

print(*result)
