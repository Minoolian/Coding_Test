# 여행 가자

# 도시의 수 N이 주어진다.
# 여행 계획에 속한 도시들의 수 M이 주어진다.
# N X N 행렬을 통해 임의의 두 도시가 연결되었는지에 관한 정보가 주어진다. 1이면 연결된 것이고 0이면 연결이 되지 않은 것이다.
# 마지막 줄에는 여행 계획이 주어진다.

import sys
input=sys.stdin.readline

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

n=int(input())
m=int(input())
parent={i:i for i in range(1, n+1)}

for y in range(1,n+1):
    lis=list(map(int,input().split()))
    for x in range(1, len(lis)+1):
        if lis[x-1]==1:
            union(y,x)

trevel=list(map(int,input().split()))
result=set([find(i) for i in trevel])
if len(result)==1:
    # 여행 경로의 모든 부모가 같다면 (연결되어있다)
    print("YES")
else:
    print("NO")