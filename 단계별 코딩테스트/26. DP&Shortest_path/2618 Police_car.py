# 경찰차

# 도로의 개수를 나타내는 정수 N, 처리해야 하는 사건의 개수를 나타내는 정수 W, 사건이 발생된 위치가 한 줄에 하나씩 주어진다.
# 두 경찰차가 이동한 총 거리, 사건이 맡겨진 경찰차 번호 1 또는 2를 출력

import sys

def dist(a,b):
    return abs(a[0]-b[0])+abs(a[1]-b[1])

n=int(sys.stdin.readline())
w=int(sys.stdin.readline())
lis=[[0]]+[list(map(int,sys.stdin.readline().split())) for _ in range(w)]

inf=sys.maxsize
dp=[[inf for _ in range(w+1)] for _ in range(w+1)]

dp[1][0]=dist([1,1],lis[1])
dp[0][1]=dist([n,n],lis[1])

for i in range(1,w+1):
    for j in range(i,w+1):
        k=j
        if i==1 and j==1:
            continue
        if k-1==i-1:
            if k-2==0:
                dp[k][i-1]=dp[k-2][i-1]+dist(lis[k],[1,1])
                dp[i-1][k]=dp[i-1][k-2]+dist(lis[k],[n,n])
            else:
                dp[k][i-1]=dp[k-2][i-1]+dist(lis[k],lis[k-2])
                dp[i-1][k]=dp[i-1][k-2]+dist(lis[k],lis[k-2])
        else:
            if k-1==0:
                dp[k][i-1]=dp[k-1][i-1]+dist(lis[k],[1,1])
                dp[i-1][k]=dp[i-1][k-1]+dist(lis[k],[n,n])
            else:
                dp[k][i-1]=dp[k-1][i-1]+dist(lis[k],lis[k-1])
                dp[i-1][k]=dp[i-1][k-1]+dist(lis[k],lis[k-1])


print(dp)