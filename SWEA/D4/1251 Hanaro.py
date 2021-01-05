# 하나로

# MST 최소신장트리를 이용한 풀이.
# https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV15StKqAQkCFAYD&categoryId=AV15StKqAQkCFAYD&categoryType=CODE
from math import sqrt
from heapq import *

def policy(a,b,e):
    L=sqrt(abs(x[a]-x[b])**2 + abs(y[a]-y[b])**2)
    return e*(L**2)

def prims(s):
    hq=[]
    visit=[True for _ in range(n)]
    visit[s]=False

    for i in cost[s]:
        heappush(hq,i)

    cnt=1
    mst=0
    while hq:
        w,v=heappop(hq)

        if visit[v]:
            visit[v]=False
            mst+=w
            cnt+=1

            for i in cost[v]:
                heappush(hq,i)
        if cnt==n:
            return mst

t=int(input())
for tc in range(1, t+1):
    n=int(input())
    x=list(map(float,input().split()))
    y=list(map(float,input().split()))
    e=float(input())
    cost=[[] for _ in range(n)]

    for i in range(n-1):
        for j in range(i+1,n):
            tmp=policy(i,j,e)
            cost[i].append([tmp,j])
            cost[j].append([tmp,i])

    print(f"#{tc} {round(prims(0))}")