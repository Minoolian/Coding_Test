# 가장 긴 증가하는 부분 수열5

# 수열 A가 주어졌을 때, 가장 긴 증가하는 부분 수열을 구하는 프로그램을 작성
# 예를 들어, 수열 A = {10, 20, 10, 30, 20, 50} 인 경우에 가장 긴 증가하는 부분 수열은 A = {10, 20, 10, 30, 20, 50} 이고, 길이는 4

# LIS 에서 저장한 DP의 값이 LIS의 실제 값이 아니란 것을 명심.

from bisect import bisect_left # 이진탐색 코드, 같은 수일 경우 왼쪽 index를 돌려준다
from collections import deque

input()
A = list(map(int, input().split()))
dp = []
result = []

for i in A:
    k = bisect_left(dp, i) #자신이 들어갈 위치 k
    if len(dp) <= k: #i가 가장 큰 숫자라면
        result.append(len(dp)) # 역추적을 위한 index 저장
        dp.append(i)
    else:
        dp[k] = i #자신보다 큰 수 중 최솟값과 대체
        result.append(k)
print(len(dp))

x=len(dp)
track=deque()
for index in range(len(result)-1, -1, -1):
    if result[index]==x-1: # 역추적하면서 값을 저장
        track.appendleft(A[index])
        x-=1
print(*track)


import bisect

def lis(arr):
    lis_arr = [arr[0]]
    res = [0]
    for n in arr[1:]:
        if lis_arr[-1] < n:
            lis_arr.append(n)
            res.append(len(lis_arr)-1)
        else:
            where = bisect.bisect_left(lis_arr, n)
            lis_arr[where] = n
            res.append(where)

    i = len(lis_arr)
    print(i)
    ans = []
    for idx in range(len(res)-1, -1, -1):
        if res[idx] == i-1:
            ans.append(arr[idx])
            i -= 1
    print(*ans[::-1])

input()
lis(list(map(int, input().split())))