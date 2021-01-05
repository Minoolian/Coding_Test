

# 별자리 만들기

# 1. 별자리를 이루는 선은 서로 다른 두 별을 일직선으로 이은 형태이다.
# 2. 모든 별들은 별자리 위의 선을 통해 서로 직/간접적으로 이어져 있어야 한다
# 선을 하나 이을 때마다 두 별 사이의 거리만큼의 비용
#
# 첫째 줄에 별의 개수 n이 주어진다.
# 둘째 줄부터 n개의 줄에 걸쳐 각 별의 x, y좌표가 실수 형태로 주어지며, 최대 소수점 둘째자리까지 주어진다.
import sys
import heapq as hq
from math import sqrt
input=sys.stdin.readline

inf=sys.maxsize

def prim(r):
    q=[]
    visited=[False for _ in range(n+1)]
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
        if cnt==n-1:
            return mst

if __name__=="__main__":
    n=int(input())
    edge=[[] for _ in range(n)]
    loc=[]

    for _ in range(n):
        x,y=map(float,input().split())
        loc.append([x,y])

    for i in range(n-1):
        for j in range(i+1,n):
            dist=round(sqrt((loc[i][0]-loc[j][0])**2+(loc[i][1]-loc[j][1])**2),2)

            edge[i].append([dist,j])
            edge[j].append([dist,i])
    print(prim(1))
