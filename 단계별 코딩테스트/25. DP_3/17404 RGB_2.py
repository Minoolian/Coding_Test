# RGB거리 2

# 1번 집부터 N번 집이 순서대로 있다.
# 집을 빨강, 초록, 파랑으로 칠하는 비용이 주어졌을 때
# 1번 집의 색은 2번, N번 집의 색과 같지 않아야 한다.
# N번 집의 색은 N-1번, 1번 집의 색과 같지 않아야 한다.
# i(2 ≤ i ≤ N-1)번 집의 색은 i-1, i+1번 집의 색과 같지 않아야 한다.

import sys

n=int(sys.stdin.readline())
lis=[list(map(int,sys.stdin.readline().split())) for _ in range(n)]
result=sys.maxsize

for color in range(3):
    dp=[[0 for _ in range(n)] for _ in range(3)]

    for i in range(3):
        if i==color:
            dp[i][0]=lis[0][i]
            continue
        dp[i][0]=result

    for i in range(1,n):
        dp[0][i] = lis[i][0] + min(dp[1][i - 1], dp[2][i - 1])
        dp[1][i] = lis[i][1] + min(dp[0][i - 1], dp[2][i - 1])
        dp[2][i] = lis[i][2] + min(dp[0][i - 1], dp[1][i - 1])


    for i in range(3):
        if i==color:
            continue
        result=min(result,dp[i][-1])

print(result)