# ★★ 가장 긴 증가하는 부분 수열2

# 수열 A가 주어졌을 때, 가장 긴 증가하는 부분 수열을 구하는 프로그램을 작성
# 예를 들어, 수열 A = {10, 20, 10, 30, 20, 50} 인 경우에 가장 긴 증가하는 부분 수열은 A = {10, 20, 10, 30, 20, 50} 이고, 길이는 4


# 모듈 미사용
# https://namu.wiki/w/%EC%B5%9C%EC%9E%A5%20%EC%A6%9D%EA%B0%80%20%EB%B6%80%EB%B6%84%20%EC%88%98%EC%97%B4
# https://jason9319.tistory.com/113
import sys

N = int(sys.stdin.readline())
A = list(map(int, sys.stdin.readline().split()))
DP = [0]

for i in range(N):

    low = 0
    high = len(DP) - 1

    while low <= high: # 현재 수 i 보다 제일 크거나 작은 수의 위치를 찾는다.
        mid = (low + high) // 2
        if DP[mid] < A[i]:
            low = mid + 1
        else:
            high = mid - 1

    if low >= len(DP): # 위치가 배열보다 크다면 넣어준다
        DP.append(A[i])
    else: # lower_bound
        DP[low] = A[i]

print(len(DP) - 1)



# 모듈 사용
from bisect import bisect_left # 이진탐색 코드, 같은 수일 경우 왼쪽 index를 돌려준다

input()
A = list(map(int, input().split()))
dp = []

for i in A:
    k = bisect_left(dp, i) #자신이 들어갈 위치 k
    if len(dp) <= k: #i가 가장 큰 숫자라면
        dp.append(i)
    else:
        dp[k] = i #자신보다 큰 수 중 최솟값과 대체
print(len(dp))
