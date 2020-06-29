# 최대 힙

# 배열에 자연수 x를 넣는다.
# 배열에서 가장 큰 값을 출력하고, 그 값을 배열에서 제거한다.

import heapq
# 파이썬 모듈은 minHeap인 heapq 를 지원한다. maxHeap으로 변경해서 사용한다.
import sys
heap = []
for _ in range(int(input())):
    num = int(sys.stdin.readline())
    if num != 0:
        heapq.heappush(heap, (-num))
    else:
        if not heap:
            print(0)
        else:
            print(-1 * heapq.heappop(heap))