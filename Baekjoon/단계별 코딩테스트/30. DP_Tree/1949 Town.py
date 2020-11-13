# 우수 마을

# N개의 마을로 이루어진 나라가 있다.
# 이 나라는 트리(Tree) 구조로 이루어져 있다. 즉 마을과 마을 사이를 직접 잇는 N-1개의 길이 있으며, 각 길은 방향성이 없다.
# 1. '우수 마을'로 선정된 마을 주민 수의 총 합을 최대로 해야 한다.
# 2. 마을 사이의 충돌을 방지하기 위해서, 만일 두 마을이 인접해 있으면 두 마을을 모두 '우수 마을'로 선정할 수는 없다. 즉 '우수 마을'끼리는 서로 인접해 있을 수 없다.
# 3. 선정되지 못한 마을에 경각심을 불러일으키기 위해서, '우수 마을'로 선정되지 못한 마을은 적어도 하나의 '우수 마을'과는 인접해 있어야 한다.

import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline
n = int(input())
w = [0] + list(map(int, input().split())) # 정점 가중치 리스트
s = [[] for i in range(n + 1)] # 간선 리스트
dp = [[0] * 2 for i in range(n + 1)]
visit = [False for i in range(n + 1)]

# dp[i][0]: 자신을 포함한, dp[i][1]: 자신을 포함하지 않은
def dfs(start):
    visit[start] = True
    # 초기 설정 및 반복 설정 (해당 정점에 대한 값 설정)
    dp[start][0] = w[start]

    for i in s[start]: # 해당 정점과 연결된 정점에 대해서
        if not visit[i]: # 방문하지 않았다면 (역행 방지)
            dfs(i)
            # 1. 해당 정점이 포함되면 다음 정점은 반드시 포함되지 않아야 한다.
            dp[start][0] += dp[i][1] # 다음 정점이 포함되지 않은 최대값과의 해당 정점의 합

            # 2. 해당 정점이 포함되지 않으면 다음 정점의 두가지 경우 중 최대값을 반영한다.
            if max(dp[i][1], dp[i][0]) == dp[i][1]:
                dp[start][1] += dp[i][1]
            else:
                dp[start][1] += dp[i][0]

for i in range(n - 1): # 간선 리스트
    a, b = map(int, input().split())
    s[a].append(b) # 무방향
    s[b].append(a)

dfs(1)

if max(dp[1][0], dp[1][1]) == dp[1][0]:
    print(dp[1][0])

else:
    print(dp[1][1])
