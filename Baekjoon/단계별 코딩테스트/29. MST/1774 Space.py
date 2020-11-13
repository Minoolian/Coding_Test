# 우주신과의 교감

# 첫째 줄에 우주신들의 개수 N, 이미 연결된 신들과의 통로의 개수 M이 주어진다.
# 두 번째 줄부터 N개의 줄에는 좌표가, 그 밑으로 M개의 줄에는 이미 연결된 통로가 주어진다.

# 첫째 줄에 만들어야 할 최소의 통로 길이를 출력하라.

import sys
from math import sqrt
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

def kruskal(g,v,c):

    g.sort(key=lambda x:x[0])# 간선을 가중치를 기준으로 정렬
    mst=0
    count=0

    for w,a,b in g:# 가중치가 작은 간선부터.
        if find(a) != find(b):
            union(a,b)
            mst+=w
            count+=1

        if count==v-1-c:# 트리를 이루면 종료.
            break

    return mst

if __name__=="__main__":
    n,m=map(int,input().split())
    edge=[]
    parent=[i for i in range(n+1)]

    loc=[]
    for _ in range(n):
        x,y=map(int,input().split())
        loc.append([x,y])

    c=0
    for _ in range(m): # 미리 연결된 간선들은 union 으로 합친다.
        u,v=map(int,input().split())
        if find(u-1) != find(v-1):
            union(u-1,v-1)
            c+=1

    for i in range(n-1):
        for j in range(i+1,n):
            dist=sqrt((loc[i][0]-loc[j][0])**2+(loc[i][1]-loc[j][1])**2)
            edge.append([dist,i,j])

    print("%.2f"%kruskal(edge,n,c))