# 행성 터널

# 터널을 총 N-1개 건설해서 모든 행성이 서로 연결되게 하려고 한다. 이때, 모든 행성을 터널로 연결하는데 필요한 최소 비용을 구하는 프로그램

# 첫째 줄에 행성의 개수 N
# 다음 N개 줄에는 각 행성의 x, y, z좌표가 주어진다.

import sys
input=sys.stdin.readline

# Union-Find를 이용하여 정점이 한 집합에 있는 지 확인
def find(x):
    if parent[x]==x:
        return x
    parent[x]=find(parent[x])
    return parent[x]

def union(x,y):
    x=find(x)
    y=find(y)

    if x!=y:
        parent[y]=x

def kruskal(g,v):

    g.sort(key=lambda x:x[0])# 간선을 가중치를 기준으로 정렬
    mst=0
    count=0

    for w,a,b in g:# 가중치가 작은 간선부터.
        if find(a) != find(b):
            union(a,b)
            mst+=w
            count+=1

        if count==v-1:# 트리를 이루면 종료.
            break

    return mst

if __name__=="__main__":
    n=int(input())
    edge=[]
    parent=[i for i in range(n+1)]
    e=[]

    for i in range(n):
        x,y,z=map(int,input().split())
        edge.append([x,y,z,i])

    for i in range(3): # 모든 간선 쌍을 확인하면 메모리 초과 / 일차원 거리중 최솟값을 찾기 위해서는 정렬한 후 인접한 값을 계산하는 것이 효율적.
        edge.sort(key=lambda x:x[i])
        cur=edge[0][3]
        for j in range(1,n):
            next=edge[j][3]
            e.append([abs(edge[j][i]-edge[j-1][i]),cur,next])
            cur=edge[j][3]

    print(kruskal(e,n))