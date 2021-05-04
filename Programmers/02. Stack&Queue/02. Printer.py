# 프린터

# queue를 이용한 풀이
# https://programmers.co.kr/learn/courses/30/lessons/42587

from collections import deque

def solution(priorities, location):
    answer = 0

    pool=deque(zip(range(len(priorities)), priorities))
    idx=1
    while pool:
        i,p=pool.popleft()

        if not pool:
            answer=idx
            break

        if p>=max(map(lambda x:x[1],pool)):
            if i==location:
                answer=idx
                break
            else:
                idx+=1
        else:
            pool.append((i,p))


    return answer

# Any 함수를 추가하여 이용한 타인 풀이

# def solution(priorities, location):
#     queue =  [(i,p) for i,p in enumerate(priorities)]
#     answer = 0
#     while True:
#         cur = queue.pop(0)
#         if any(cur[1] < q[1] for q in queue):
#             queue.append(cur)
#         else:
#             answer += 1
#             if cur[0] == location:
#                 return answer