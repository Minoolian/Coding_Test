# 특정한 최단 경로

# 임의로 주어진 두 정점은 반드시 통과하면서 1번 정점에서 N번 정점으로의 최단거리

# 3번의 다익스트라 알고리즘으로 해결.

import sys
import heapq

inf=sys.maxsize

v,e=map(int,sys.stdin.readline().split())
lis=[[] for _ in range(v+1)]

def dijkstra(start):

    dp = [inf] * (v + 1)
    dp[start]=0

    h = []
    heapq.heappush(h,[0, start])

    while h:
        w, n=heapq.heappop(h)
        for nn,ww in lis[n]:
            nw=ww+w
            if nw<dp[nn]:
                dp[nn]=nw
                heapq.heappush(h,[nw,nn])

    return dp

for _ in range(e):
    a,b,c=map(int,sys.stdin.readline().split())
    lis[a].append([b,c])
    lis[b].append([a,c]) # 방향성이 없다.
v1, v2=map(int,sys.stdin.readline().split())

S=dijkstra(1) # 정점 1부터 모든 정점까지의 최소거리
v_1=dijkstra(v1) # 정점 v1 부터 모든 정점까지의 최소거리
v_2=dijkstra(v2) # 정점 v2 부터 모든 정점까지의 최소거리

result=min(S[v1]+v_1[v2]+v_2[v], S[v2]+v_2[v1]+v_1[v])
# 1 - v1 - v2 - v / 1 - v2 - v1 - v 중에서 최솟값

print(result if result<inf else -1)