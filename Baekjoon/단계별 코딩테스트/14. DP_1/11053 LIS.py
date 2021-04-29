# LIS(Longest Increasing Subsequence)
# 수열 A가 주어졌을 때, 가장 긴 증가하는 부분 수열을 구하는 프로그램을 작성하시오.
# 예를 들어, 수열 A = {10, 20, 10, 30, 20, 50} 인 경우에 가장 긴 증가하는 부분 수열은 {10, 20, 30, 50} 이고, 길이는 4이다.

import sys

n=int(sys.stdin.readline())

lis=list(map(int,sys.stdin.readline().split()))
dp=[1 for i in range(n)]

for i in range(n):
    for j in range(i): # 처음부터 해당 인덱스 전까지 검사
        if lis[i] > lis[j]: # 해당 인덱스의 값보다 작은 값이 있으면
            dp[i]=max(dp[i],dp[j]+1) # 수열이 이루어지므로 고려한다.

print(max(dp))

