# 경찰차

# 도로의 개수를 나타내는 정수 N, 처리해야 하는 사건의 개수를 나타내는 정수 W, 사건이 발생된 위치가 한 줄에 하나씩 주어진다.
# 두 경찰차가 이동한 총 거리, 사건이 맡겨진 경찰차 번호 1 또는 2를 출력

import sys

def dist(a,b):
    return (abs(a[0]-b[0])**2+abs(a[1]-b[1])**2)**0.5

n=int(sys.stdin.readline())
w=int(sys.stdin.readline())
lis=[list(map(int,sys.stdin.readline().split())) for _ in range(w)]

inf=sys.maxsize
dp=[[inf for _ in range(n+1)] for _ in range(n+1)]

dp[1][0]=dist([1,1],lis[0])
dp[0][1]=dist([n,n],lis[0])

for i in range(2,)