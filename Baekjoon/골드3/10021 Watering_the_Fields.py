# Watering the Fields

# MST 풀이
# https://www.acmicpc.net/problem/10021

# Kruskal's

import heapq as hq

def Euclidean(a,b):
    return (a[0]-b[0])**2+(a[1]-b[1])**2

def find(x):
    if parent[x]==x:
        return x

    return find(parent[x])

def union(x, y):
    x=find(x)
    y=find(y)

    if x!=y:
        parent[y]=x


N,C=map(int,input().split())
index=[[] for _ in range(N)]
edge=[]
parent=[i for i in range(N)]

for i in range(N):
    x,y=map(int, input().split())
    index[i]=[x,y]

for i in range(N-1):
    for j in range(i+1,N):
        dis=Euclidean(index[i],index[j])
        if dis>=C:
            hq.heappush(edge,[dis,i,j])

edge.sort()
mst=0
e=0

while edge:
    w,a,b=hq.heappop(edge)
    if find(a) != find(b):
        union(a,b)
        mst+=w
        e+=1

    if e==N-1:
        break

print(mst) if e==N-1 else print(-1)




# Prims
# import heapq as hq
#
# def Euclidean(a,b):
#     return (a[0]-b[0])**2+(a[1]-b[1])**2
#
#
# N,C=map(int,input().split())
# index=[[] for _ in range(N)]
# edge=[[] for _ in range(N)]
#
# for i in range(N):
#     x,y=map(int, input().split())
#     index[i]=[x,y]
#
# for i in range(N-1):
#     for j in range(i+1,N):
#         dis=Euclidean(index[i],index[j])
#         edge[i].append([dis,j])
#         edge[j].append([dis,i])
#
# q=[]
# visit=[True for _ in range(N)]
# visit[0]=False
#
# e=0
# mst=0
#
# for i in edge[0]:
#     hq.heappush(q,i)
#
# while q:
#     w,u=hq.heappop(q)
#
#     if visit[u] and w>=C:
#         visit[u]=False
#         e+=1
#         mst+=w
#
#         for i in edge[u]:
#             hq.heappush(q, i)
#
#     if e==N-1:
#         break
# print(mst) if e==N-1 else print(-1)




