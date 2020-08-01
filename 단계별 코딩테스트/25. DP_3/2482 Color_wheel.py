# 색상환

# N과 K에 대하여, N개의 색으로 구성되어 있는 색상환에서
# 어떤 인접한 두 색도 동시에 선택하지 않으면서 서로 다른 K개의 색을 선택하는 경우의 수를 구하는 프로그램

import sys

mod=1000000003
inf=sys.maxsize
n=int(sys.stdin.readline()); k=int(sys.stdin.readline())
dp=[[0]*(k+1) for _ in range(n+1)]

for i in range(n+1):
    dp[i][1] = i;
    dp[i][0] = 1;

for i in range(2,n+1):
    for j in range(2,k+1):
        dp[i][j]=(dp[i-2][j-1] + dp[i-1][j])%mod

result=(dp[n-1][k] + dp[n-3][k-1])%mod
print(result)