import sys

n=int(sys.stdin.readline())
dp=[0]*1000001
dp[1]=1
dp[2]=2

for i in range(3,n+1):
    dp[i]=(dp[i-1]+dp[i-2])%15746
    # (x+y) % mod = (x%mod + y%mod) %mod
    # (x%mod + y%mod) != (x+y)%mod
print(dp[n])

# memoization 없이 빠르게 수행하는 방법
# import sys
# n = int(sys.stdin.readline())
# f = 1
# s = 2
# tmp = 0
# for i in range(n - 1):
#     tmp = f
#     f = s
#     s = (tmp + s) % 15746
# print(f)