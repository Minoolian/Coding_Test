# 행렬 곱셈 순서

# 크기가 N×M인 행렬 A와 M×K인 B를 곱할 때 필요한 곱셈 연산의 수는 총 N×M×K번이다.
# 행렬 N개를 곱하는데 필요한 곱셈 연산의 수는 행렬을 곱하는 순서에 따라 달라지게 된다.

import sys

n=int(sys.stdin.readline())
lis=[list(map(int,sys.stdin.readline().split())) for _ in range(n)]

dp=[[0 for _ in range(n+1)] for _ in range(n+1)] # NXN memoization
# dp[i][j]: i번째부터 j번째까지의 최소 행렬곱

for x in range(1,n+1): # 최종 결과를 얻기 위해서는 우측 아래로 대각선으로 먼저 채워나가야 한다. (x는 자리 잡기위한 용도)
    for i in range(n-x): # 대각선은 점점 줄어듦으로 x만큼 줄인다.
        j=i+x # 대각선 원소의 i와 j는 고정된 x만큼의 차이가 난다.
        dp[i][j]=sys.maxsize
        for k in range(i,j):
            dp[i][j]=min(dp[i][j],dp[i][k]+dp[k+1][j]+(lis[i][0]*lis[k][1]*lis[j][1]))

print(dp[0][n-1])