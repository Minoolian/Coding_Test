# 디스크 컨트롤러

#
# https://programmers.co.kr/learn/courses/30/lessons/42627

import heapq as hq

def solution(jobs):
    answer = 0

    n=len(jobs)
    t_jobs=[[b,a] for a,b in jobs]
    hq.heapify(t_jobs)
    hq.heapify(jobs)

    cur=0
    temp=[]

    while jobs:
        if cur<=jobs[0][0]:
            s,t=hq.heappop(jobs)
            t_jobs.remove([t,s])
            hq.heapify(t_jobs)
            answer+=t
            cur=s+t
        else:
            while True:
                t,s=hq.heappop(t_jobs)
                if s<cur:
                    jobs.remove([s,t])
                    hq.heapify(jobs)
                    answer+=(cur-s)+t
                    cur+=t
                    while temp:
                        hq.heappush(t_jobs, temp.pop())

                    break
                else:
                    temp.append([t,s])

    return answer//n

print(solution([[0, 10], [4, 10], [15, 2], [5, 11]]))


# import heapq as hq
# from collections import deque
# from copy import deepcopy
#
# def solution(jobs):
#     answer = 0
#
#     n=len(jobs)
#     t_jobs=[[b,a] for a,b in jobs]
#     s_jobs=deepcopy(jobs)
#     jobs=deque(jobs)
#     hq.heapify(t_jobs)
#     # while t_jobs:
#     #     print(hq.heappop(t_jobs))
#     hq.heapify(s_jobs)
#
#     cur=0
#     temp=[]
#
#     while jobs:
#         if cur<=s_jobs[0][0]:
#             s,t=jobs.popleft()
#             s_jobs.remove([s,t])
#             t_jobs.remove([t,s])
#             hq.heapify(s_jobs)
#             hq.heapify(t_jobs)
#             answer+=t
#             cur=s+t
#         else:
#             while True:
#                 t,s=hq.heappop(t_jobs)
#                 if s<cur:
#                     jobs.remove([s,t])
#                     s_jobs.remove([s,t])
#                     hq.heapify(s_jobs)
#                     answer+=(cur-s)+t
#                     cur+=t
#                     while temp:
#                         hq.heappush(temp.pop())
#
#                     break
#                 else:
#                     temp.append([t,s])
#
#     return answer//n

# print(solution([[0, 3], [1, 9], [2, 6]]))