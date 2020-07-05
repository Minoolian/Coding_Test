# 앱

# 앱 Ai는 각각 mi 바이트만큼의 메모리를 사용하고 있다
# 앱 Ai를 비활성화한 후에 다시 실행하고자 할 경우, 추가적으로 들어가는 비용(시간 등)을 수치화 한 것을 ci
#  M 바이트의 메모리가 필요하다고 하자. 즉, 현재 활성화 되어 있는 앱 A1, ..., AN 중에서 몇 개를 비활성화 하여 M 바이트 이상의 메모리를 추가로 확보

# 기존 0-1 Knapsack 문제와 상당히 유사하다.
# 열은 비활성화 했을때의 최소 cost를 찾기 위한 증가, 행은 각 앱을 비활성화 했을때의 c, 값은 비활성화 했을때 누적되는 최대 byte

import sys

n,m=map(int,sys.stdin.readline().split())
a=[0]+list(map(int,sys.stdin.readline().split()))
c=[0]+list(map(int,sys.stdin.readline().split()))
dp=[[0 for _ in range(sum(c)+1)] for _ in range(n+1)]

if m==0:
    print(0)
else:
    for j in range(1,sum(c)+1):
        for i in range(1,n+1):
            byte = a[i]
            cost = c[i]

            if j<cost:
                dp[i][j]=dp[i-1][j]
            else:
                dp[i][j]=max(byte+dp[i-1][j-cost], dp[i-1][j])

            if dp[i][j]>=m:
                print(j)
                exit(0)



