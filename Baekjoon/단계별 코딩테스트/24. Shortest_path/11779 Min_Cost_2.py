
# 최소비용 구하기2

# 첫째 줄에 도시의 개수 n(1≤n≤1,000)이 주어지고, 둘째 줄에는 버스의 개수 m(1≤m≤100,000)이 주어진다.
# 그리고 셋째 줄부터 m+2줄까지 다음과 같은 버스의 정보가 주어진다. 먼저 처음에는 그 버스의 출발 도시의 번호가 주어진다.
import sys
import heapq
from collections import deque

inf=sys.maxsize

v=int(sys.stdin.readline())
e=int(sys.stdin.readline())
lis=[[] for _ in range(v+1)]
dp=[[inf,inf] for _ in range(v+1)]
h=[]

def dijkstra(start):
    dp[start][0]=0
    heapq.heappush(h,[0, start])

    while h:
        w, n=heapq.heappop(h)
        for nn,ww in lis[n]:
            nw=ww+w
            if nw<dp[nn][0]:
                dp[nn][0]=nw
                dp[nn][1]=n
                heapq.heappush(h,[nw,nn])

for _ in range(e):
    u,v,w=map(int,sys.stdin.readline().split())
    lis[u].append([v,w])
s,k=map(int,sys.stdin.readline().split())

dijkstra(s)

print(dp[k][0])
result=deque([k])
while dp[k][1]!=inf:
    result.appendleft(dp[k][1])
    k=dp[k][1]
print(len(result))
print(*result)