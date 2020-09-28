# 사회망 서비스(SNS)

# 얼리 아답터가 아닌 사람들은 자신의 모든 친구들이 얼리 아답터일 때만 이 아이디어를 받아들인다.
# 가능한 한 최소의 수의 얼리 아답터를 확보하여 모든 사람이 이 아이디어를 받아들이게 하는 문제

import sys
sys.setrecursionlimit(10**6)
input=sys.stdin.readline

n=int(input())
tree=[[] for _ in range(n+1)]

for _ in range(n-1):
    u,v= map(int,input().split())
    tree[u].append(v)
    tree[v].append(u)

dp=[[0,0] for _ in range(n+1)]
check=[False for _ in range(n+1)]

def dfs(cur):
    check[cur]=True
    dp[cur][0]=1 # 해당 노드를 포함할 때
    dp[cur][1]=0 # 해당 노드를 포함하지 않을 때
    for i in tree[cur]:
        if not check[i]:
            dfs(i)
            dp[cur][0]+=dp[i][1]
            dp[cur][1]+=max(dp[i][0],dp[i][1])

dfs(1)
print(n-max(dp[1][0],dp[1][1]))