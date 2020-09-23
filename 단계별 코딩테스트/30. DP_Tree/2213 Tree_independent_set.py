# 트리의 독립집합

# 그래프 G(V, E)에서 정점의 부분 집합 S에 속한 모든 정점쌍이 서로 인접하지 않으면 (정점쌍을 잇는 에지가 없으면) S를 독립 집합(independent set)이라고 한다.
# 트리(연결되어 있고 사이클이 없는 그래프)와 각 정점의 가중치가 양의 정수로 주어져 있을 때, 최대 독립 집합을 구하는 것

# 트리의 정점의 수 n
# n개의 정수 w1, w2, ..., wn이 주어지는데, wi는 정점 i의 가중치
# 셋째 줄부터 마지막 줄까지는 에지 리스트가 주어지는데, 한 줄에 하나의 에지를 나타낸다. 에지는 정점의 쌍으로 주어진다.

import sys
input = sys.stdin.readline
n = int(input())
w = [0] + list(map(int, input().split())) # 정점 가중치 리스트
s = [[] for i in range(n + 1)] # 간선 리스트
dp = [[0] * 2 for i in range(n + 1)]
visit = [False for i in range(n + 1)]
num = [[[], []] for i in range(n + 1)]

# dp[i][0]: 자신을 포함한, dp[i][1]: 자신을 포함하지 않은
def dfs(start):
    visit[start] = True
    # 초기 설정 및 반복 설정 (해당 정점에 대한 값 설정)
    dp[start][0] = w[start]
    num[start][0].append(start)
    for i in s[start]: # 해당 정점과 연결된 정점에 대해서
        if not visit[i]: # 방문하지 않았다면 (역행 방지)
            dfs(i)
            # 1. 해당 정점이 포함되면 다음 정점은 반드시 포함되지 않아야 한다.
            dp[start][0] += dp[i][1] # 다음 정점이 포함되지 않은 최대값과의 해당 정점의 합
            for j in num[i][1]: # 다음 정점이 포함되지 않은 집합
                num[start][0].append(j)

            # 2. 해당 정점이 포함되지 않으면 다음 정점의 두가지 경우 중 최대값을 반영한다.
            if max(dp[i][1], dp[i][0]) == dp[i][1]:
                dp[start][1] += dp[i][1]
                for k in num[i][1]:
                    num[start][1].append(k)
            else:
                dp[start][1] += dp[i][0]
                for k in num[i][0]:
                    num[start][1].append(k)

for i in range(n - 1): # 간선 리스트
    a, b = map(int, input().split())
    s[a].append(b) # 무방향
    s[b].append(a)

dfs(1)

if max(dp[1][0], dp[1][1]) == dp[1][0]:
    print(dp[1][0])
    a = num[1][0]
    a.sort()
    print(*a)
else:
    print(dp[1][1])
    a = num[1][1]
    a.sort()
    print(*a)