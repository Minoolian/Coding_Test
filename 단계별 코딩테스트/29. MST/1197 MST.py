# 최소 스패닝 트리

# 정점의 개수 V와 간선의 개수 E가 주어진다.
# 다음 E개의 줄에는 각 간선에 대한 정보를 나타내는 세 정수 A, B, C가 주어진다. 이는 A번 정점과 B번 정점이 가중치 C인 간선으로 연결되어 있다는 의미이다.
# C는 음수일 수도 있으며, 절댓값이 1,000,000을 넘지 않는다.

# Kruskal's 알고리즘
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

def kruskal(g,v,e):

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
    v,e=map(int,input().split())
    edge=[]
    parent=[i for i in range(v+1)]

    for _ in range(e):
        a,b,c=map(int,input().split())
        edge.append([c,a,b])

    print(kruskal(edge,v,e))

# Prim's 알고리즘
# 우선순위 큐를 이용하여 최소 정점을 알아낸다.
import sys
import heapq as hq
input=sys.stdin.readline

inf=sys.maxsize

def prim(r):
    q=[]
    visited=[False for _ in range(v+1)]
    visited[r]=True

    cnt=0
    mst=0

    for i in edge[r]:
        hq.heappush(q,i)

    while q:
        w,u=hq.heappop(q)

        if not visited[u]:
            visited[u]=True
            cnt+=1
            mst+=w

            for i in edge[u]:
                hq.heappush(q,i)
        if cnt==v-1:
            return mst

if __name__=="__main__":
    v,e=map(int,input().split())
    edge=[[] for _ in range(v+1)]

    for _ in range(e):
        a,b,c=map(int,input().split())
        edge[a].append([c,b])
        edge[b].append([c,a])

    print(prim(1))



