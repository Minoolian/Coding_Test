# 이중 우선순위 큐

# 두개의 힙을 이용한 풀이
# https://programmers.co.kr/learn/courses/30/lessons/42628

import heapq as hq

def solution(operations):
    min_q = []
    max_q = []

    for cmd in operations:
        if cmd[0]=='I':
            cmd=int(cmd[2:])
            hq.heappush(min_q,cmd)
            hq.heappush(max_q,-cmd)
        elif cmd[0]=='D' and max_q:
            cmd=int(cmd[2:])
            if cmd==1:
                min_q.remove(-hq.heappop(max_q))
            else:
                max_q.remove(-hq.heappop(min_q))

    return [-hq.heappop(max_q),hq.heappop(min_q)] if max_q else [0,0]

print(solution(["I 16", "I -5643", "D -1", "D 1", "D 1", "I 123", "D -1"]))