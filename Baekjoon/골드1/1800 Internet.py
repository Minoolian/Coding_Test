# 인터넷 설치

# 다익스트라 & 이분탐색 풀이
# https://www.acmicpc.net/problem/1800

import heapq as hq

def dijkstra(s, limit):
    q=[]
    distance=[float('inf')]*(N+1)
    hq.heappush(q,[0,s])
    distance[s]=0

    while q:
        cost, idx=hq.heappop(q)

        for a in internet[idx]:
            if a[1]>limit:
                if cost+1<distance[a[0]]:
                    distance[a[0]]=cost+1
                    hq.heappush(q,[cost+1, a[0]])
            else:
                if cost<distance[a[0]]:
                    distance[a[0]]=cost
                    hq.heappush(q,[cost, a[0]])

    return False if distance[N]>K else True


N,P,K=map(int,input().split())
internet=[[] for _ in range(N+1)]
for _ in range(P):
    u,v,cc=map(int,input().split())
    internet[u].append([v,cc])
    internet[v].append([u,cc])

left, right=0, 1000001
answer=float('inf')

while left<=right:
    mid=(left+right)//2
    if dijkstra(1, mid):
        right=mid-1
        answer=mid
    else:
        left=mid+1

if answer==float('inf'):
    print(-1)
else:
    print(answer)



# 잘못된 접근
# import heapq as hq
# 
# N,P,K=map(int,input().split())
# internet=[[] for _ in range(N+1)]
# for _ in range(P):
#     u,v,cc=map(int,input().split())
#     internet[u].append([v,cc])
#     internet[v].append([u,cc])
# 
# c=[[float('inf'),float('inf')] if i!=1 else [0,0] for i in range(N+1)]
# q=[]
# hq.heappush(q, [0, 1, 1])
# while q:
#     cost, n, free=hq.heappop(q)
#     f=1 if free else 0
# 
#     for nn, ww in internet[n]:
#         nw=max(cost, ww)
#         if c[nn][f]>nw:
#             c[nn][f]=nw
#             hq.heappush(q, [nw, nn, free])
#         
#         if free-1==0: 
#             f=0
#         if free and c[nn][f]>cost:
#             c[nn][f]=cost
#             hq.heappush(q, [cost, nn, free-1])
# print(c)