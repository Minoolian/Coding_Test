# 최단경로

# 그래프가 주어지면 주어진 시작점에서 다른 모든 정점으로의 최단 경로를 구하는 프로그램
# 정점의 개수 V와 간선의 개수 E가 주어진다. 둘째 줄에는 시작 정점의 번호 K
# u에서 v로 가는 가중치 w인 간선이 존재한다

# 다익스트라 알고리즘을 수행할 때 인접행렬을 이용하는 방법은 시간복잡도면에서 큰 손실이 있을 수 있지만, 우선순위 큐를 활용하면 비용을 줄일 수 있다.
import sys
import heapq

inf=sys.maxsize

v,e=map(int,sys.stdin.readline().split())
k=int(sys.stdin.readline())
lis=[[] for _ in range(v+1)]
dp=[inf]*(v+1)
h=[]

def dijkstra(start):
    dp[start]=0
    heapq.heappush(h,[0, start])

    while h:
        w, n=heapq.heappop(h)
        for nn,ww in lis[n]:
            nw=ww+w
            if nw<dp[nn]:
                dp[nn]=nw
                heapq.heappush(h,[nw,nn])

for _ in range(e):
    u,v,w=map(int,sys.stdin.readline().split())
    lis[u].append([v,w])

dijkstra(k)

for i in dp[1:]:
    print(i if i!=inf else "INF")