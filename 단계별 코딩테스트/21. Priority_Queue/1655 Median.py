# 가운데를 말해요

# 수 중에서 중간값을 찾는다.
# 만약, 개수가 짝수개라면 중간에 있는 두 수 중에서 작은 수를 찾는다.

import sys
import heapq

n=int(sys.stdin.readline())
max_h=[] # 최대힙 (작은 수들의 모임)
min_h=[] # 최소힙 (큰 수들의 모임)

for _ in range(n):
    a=int(sys.stdin.readline())

    if len(max_h)==len(min_h): # 최대힙에 우선 삽입
        heapq.heappush(max_h, (-a, a))
    else:
        heapq.heappush(min_h, (a, a))

    if min_h and min_h[0][1] < max_h[0][1]:
        # 최대힙의 값이 최소힙의 값보다 크면 안되므로 두 자리를 변경한다.
        c=heapq.heappop(min_h)[1]
        d=heapq.heappop(max_h)[1]
        heapq.heappush(min_h, (d, d))
        heapq.heappush(max_h, (-c, c))

    print(max_h[0][1])