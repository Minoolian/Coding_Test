# 더 맵게

# Heap을 이용한 풀이
# https://programmers.co.kr/learn/courses/30/lessons/42626

import heapq as hq

def solution(scoville, K):
    answer = 0
    hq.heapify(scoville)

    while True:
        a=hq.heappop(scoville)
        if a>=K:
            return answer
        if scoville:
            answer+=1
            b=hq.heappop(scoville)
        else:
            return -1

        new=a+b*2
        hq.heappush(scoville,new)

    return answer

print(solution([1,2,3,9,10,12],7))