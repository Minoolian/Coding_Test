# KCM Travel

# 최대 M원의 비용 지원, 각 공항들 간 티켓가격과 이동시간이 주어질때 가장빠른길을 찾는다.
# 공항의수 N, 지원비용 M, 티켓정보의  수 K, (u,v,c,d): 출발,도착,비용,시간 이 주어진다.
# 출발은 1, 도착은 N이다.

import sys

inf=sys.maxsize
t= int(sys.stdin.readline())

while t:
    t-=1
    n,m,k=map(int,sys.stdin.readline().split())
    ap=[[] for _ in range(n+1)]
    for i in range(k):
        u,v,c,d=map(int,sys.stdin.readline().split())
        ap[u].append([v,c,d])

    dp=[[inf]*(m+1) for _ in range(n+1)]

    for i in range(m+1):
        for j in range(1,n+1):
            if dp[j][i]==inf:
                continue
            temp=dp[j][i]
            for v,c,d in dp[j]:
                if c+i>m:
                    continue
                dp[v][c+i]=min(dp[v][c+i],temp+d)
    k=min(dp[n])

