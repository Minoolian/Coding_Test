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