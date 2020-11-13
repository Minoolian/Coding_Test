# 2579 계단 오르기 문제와 유사하다. 단 현재 x번째 와인을 마시지 않는 경우도 고려해야 한다.
import sys

N=int(sys.stdin.readline())
amount=[0 for i in range(10000)]
dp=[0 for _ in range(10000)]

for i in range(N):
    amount[i]=int(sys.stdin.readline())

# N=1 일 경우 때문에 amount, dp 리스트를 미리 최대값까지 잡아야 런타임 오류가 나지 않는다.
dp[0]=amount[0]
dp[1]=amount[0]+amount[1]

for n in range(2,N):
    dp[n]=max(dp[n-1],amount[n]+dp[n-2],amount[n]+amount[n-1]+dp[n-3])

print(dp[N-1])
