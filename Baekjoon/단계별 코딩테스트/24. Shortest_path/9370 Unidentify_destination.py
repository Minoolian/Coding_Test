# 미확인 도착지

# s지점에서 출발했으며 목적지 후보들 중 하나가 그들의 목적지이다.
# g와 h 교차로 사이에 있는 도로를 지나갔다는 것, 목적지들을 공백으로 분리시킨 오름차순의 정수들로 출력

import sys
from heapq import heappush, heappop

inf=sys.maxsize

def dijkstra(start):
    dp=[inf]*(n+1)
    dp[start]=0

    h=[]
    heappush(h,[0,start])

    while h:
        w,x=heappop(h)
        for nn, ww in lis[x]:
            nw=ww+w
            if dp[nn] > nw:
                dp[nn]=nw
                heappush(h,[nw,nn])

    return dp


for _ in range(int(sys.stdin.readline())):

    n,m,t=map(int,sys.stdin.readline().split())
    s,g,h=map(int,sys.stdin.readline().split())

    lis=[[] for _ in range(n+1)]

    for _ in range(m):
        a,b,d=map(int,sys.stdin.readline().split())
        lis[a].append([b,d])
        lis[b].append([a,d])

    des=[int(sys.stdin.readline()) for _ in range(t)] # 도착 후보지 두 곳

    st=dijkstra(s)
    v1=dijkstra(g)
    v2=dijkstra(h)

    fin_lis=[]
    for i in des:
        result = min(st[g] + v1[h] + v2[i], st[h] + v2[g] + v1[i])
        if result == st[i]:
        # 지나갔을 것으로 예정되는 길을 갔을 때의 최단경로와 단순히 최단경로를 구했을 때
        # 그 값이 같다면, 원래 최단경로의 일부에 이 길이 포함되어 있다는 것을 의미한다.
            fin_lis.append(i)

    fin_lis.sort()
    print(*fin_lis)

