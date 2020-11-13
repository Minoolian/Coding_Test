import sys

N=int(sys.stdin.readline())
stair=[0 for i in range(300)]
dp=[0 for _ in range(300)]

for i in range(N):
    stair[i]=int(sys.stdin.readline())

# N=1 일 경우 때문에 stair, dp 리스트를 미리 최대값까지 잡아야 런타임 오류가 나지 않는다.
dp[0]=stair[0]
dp[1]=stair[0]+stair[1]
dp[2]=max(stair[1]+stair[2],stair[0]+stair[2])

for n in range(3,N):
    dp[n]=max(stair[n]+dp[n-2],stair[n]+stair[n-1]+dp[n-3])

print(dp[N-1])
