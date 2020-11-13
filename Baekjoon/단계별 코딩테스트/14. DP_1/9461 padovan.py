# i번째의 원소가 i-2 + i-3 의 규칙으로 이루어져 있다.ㄴ
import sys

dp = [0 for _ in range(101)]
dp[1] = 1
dp[2] = 1
dp[3] = 1

for i in range(4, 101):
    dp[i] = dp[i - 2] + dp[i - 3]

t=int(sys.stdin.readline())
for _ in range(t):
    n=int(sys.stdin.readline())
    print(dp[n])