# 최종 순위

# 첫째 줄에는 테스트 케이스의 개수가 주어진다.
# 팀의 수 n을 포함하고 있는 한 줄.
# n개의 정수 ti를 포함하고 있는 한 줄. ti는 작년에 i등을 한 팀의 번호이다. 1등이 가장 성적이 높은 팀이다. 모든 ti는 서로 다르다.
# 상대적인 등수가 바뀐 쌍의 수 m
# 두 정수 ai와 bi를 포함하고 있는 m줄. 상대적인 등수가 바뀐 두 팀이 주어진다. 같은 쌍이 여러 번 발표되는 경우는 없다.

import sys
from collections import deque
input=sys.stdin.readline

t=int(input())

for _ in range(t):
    n=int(input())
    rank=list(map(int,input().split()))
    indegree=[0 for _ in range(n+1)]
    g=[[] for _ in range(n+1)]
    q=deque()

    for i in range(n-1): # 작년 순위를 토대로 인접행렬 구성
        for j in range(i+1,n):
            g[rank[i]].append(rank[j])
            indegree[rank[j]]+=1

    m=int(input())
    for _ in range(m):
        a,b=map(int,input().split())
        chk=True

        for i in g[a]:
            if i==b: # a가 높은 순위
                g[a].remove(b)
                g[b].append(a)
                indegree[a]+=1
                indegree[b]-=1
                chk=False
        if chk:
            g[b].remove(a)
            g[a].append(b)
            indegree[a]-=1
            indegree[b]+=1

    for i in range(1, n+1):
        if indegree[i]==0:
            q.append(i)

    result=[]
    flag=0
    if not q:
        flag=1
    while q:
        if len(q)>1: # q에 두개이상 들어오면 순위를 확정할 수 없다.
          flag=1
          break

        h=q.popleft()
        result.append(h)
        for i in g[h]:
            indegree[i]-=1
            # 간선 삭제
            if indegree[i]==0:
            # 추가로 발견되는 들어오는 간선이 없는 정점을 q에 삽입
                q.append(i)
            elif indegree[i]<0: # 사이클 탐지
                flag=1
                break


    if flag>0 or len(result)<n:
        print("IMPOSSIBLE")
    else:
        print(*result)



