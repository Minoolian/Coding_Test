import sys

n=int(sys.stdin.readline())

dp=[list(map(int,sys.stdin.readline().split())) for _ in range(n)]

for i in range(1,n):
    dp[i][0]=min(dp[i-1][1],dp[i-1][2])+dp[i][0]
    dp[i][1]=min(dp[i-1][0],dp[i-1][2])+dp[i][1]
    dp[i][2]=min(dp[i-1][0],dp[i-1][1])+dp[i][2]
# i번째 집의 각 색에 따라 i-1 번째의 비용을 더해서 비교한다.

print(min(dp[n-1][0],dp[n-1][1],dp[n-1][2]))