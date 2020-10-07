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

        for i in g[a]:
            if i==b:
