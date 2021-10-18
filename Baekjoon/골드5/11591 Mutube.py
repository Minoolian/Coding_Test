# MooTube

# BFS를 이용ㅇ한 풀이
# https://www.acmicpc.net/problem/15591

from collections import deque

n,qq=map(int,input().split())
tree=[[] for _ in range(n+1)]

for _ in range(n-1):
    p,q,r=map(int,input().split())
    tree[p].append([q,r])
    tree[q].append([p,r])

for _ in range(qq):
    k,v=map(int,input().split())
    answer=0

    q=deque([[v,float('inf')]])
    visit=[True for _ in range(n+1)]
    visit[v]=False
    while q:
        vv,u=q.popleft()

        for t in tree[vv]:
            if visit[t[0]]:
                visit[t[0]]=False
                n_u= t[1] if t[1]<u else u
                q.append([t[0],n_u])
                if n_u>=k:
                    answer+=1

    print(answer)