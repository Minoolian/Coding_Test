# 절댓값 힙

# 배열에 정수 x (x ≠ 0)를 넣는다.
# 배열에서 절댓값이 가장 작은 값을 출력하고, 그 값을 배열에서 제거한다. 절댓값이 가장 작은 값이 여러개일 때는, 가장 작은 수를 출력하고, 그 값을 배열에서 제거한다.

import sys
import heapq

n=int(sys.stdin.readline())
heap=[]

for _ in range(n):
    num=int(sys.stdin.readline())
    if num!=0:
        heapq.heappush(heap,(abs(num),num)) # heap을 튜플로 구성
    else:
        if len(heap)!=0:
            print(heapq.heappop(heap)[1]) # 원래 값을 출력
        else:
            print(0)