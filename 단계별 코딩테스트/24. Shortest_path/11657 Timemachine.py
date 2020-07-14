# 타임머신

# N개의 도시, M개의 버스 (A~B 까지 걸리는 시간 C)
# 1번 도시에서 출발해 나머지 모든 도시의 최단 시간을 구하라.
# 음의 사이클이 존재한다면 -1

# 다익스트라 알고리즘과 조금 유사하지만, 시간복잡도가 크다.

import sys

inf=sys.maxsize

n,m=map(int,sys.stdin.readline().split())
bus=[[] for _ in range(n+1)]
for _ in range(m):
    a,b,c=map(int,sys.stdin.readline().split())
    bus[a].append([b,c])

dp=[inf]*(n+1)

def bellmanford():
    dp[1]=0
    for i in range(1,n+2):
        for s in range(1,n+1): # 모든간선에 대해서
            for e,t in bus[s]: # s에 해당하는 모든 간선 추출
                if dp[s]!=inf and dp[e] > dp[s]+t:
                    if i==n+1: # 정점의 수 보다 많이 돌면 음의사이클이 존재
                        print(-1)
                        exit(0)
                    else:
                        dp[e]=dp[s]+t

bellmanford()
for i in range(2,n+1):
    if dp[i]<inf:
        print(dp[i])
    else:
        print(-1)