# ACM Craft

# 테스트케이스의 개수 T가 주어진다
# 첫째 줄에 건물의 개수 N 과 건물간의 건설순서규칙의 총 개수 K이 주어진다.
# 둘째 줄에는 각 건물당 건설에 걸리는 시간 D가 공백을 사이로 주어진다.
# 셋째 줄부터 K+2줄까지 건설순서 X Y가 주어진다.
# 마지막 줄에는 백준이가 승리하기 위해 건설해야 할 건물의 번호 W가 주어진다.

import sys
from collections import deque
input=sys.stdin.readline

t=int(input())

for _ in range(t):
    n,k=map(int,input().split())
    time=[0]+list(map(int,input().split()))
    indegree=[0 for _ in range(n+1)]
    g=[[] for _ in range(n+1)]
    dp=[0 for _ in range(n+1)]

    for _ in range(k):
        a,b=map(int,input().split())
        g[a].append(b)
        indegree[b]+=1

    q=deque()
    target=int(input())

    for i in range(1, n+1):
        if indegree[i]==0:
            q.append(i)
            dp[i]=time[i]

    while q:
        h=q.popleft()

        for i in g[h]:
            indegree[i]-=1
            dp[i]=max(dp[h]+time[i], dp[i])
            # 동적계획법으로 건물 짓는 시간을 저장한다. (최소시간이 아닌 크게 걸린시간)
            if indegree[i]==0:
                q.append(i)

    print(dp[target])


