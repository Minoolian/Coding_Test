# 기능개발

# 큐를 이용한 풀이
# https://programmers.co.kr/learn/courses/30/lessons/42586?language=python3

from collections import deque

def solution(progresses, speeds):
    answer = []
    p=deque(progresses)
    s=deque(speeds)

    while p:
        complete=0
        flag=True
        for _ in range(len(p)):
            pp,ss=p.popleft(), s.popleft()
            if pp+ss>=100 and flag:
                complete+=1
            else:
                p.append(pp+ss)
                s.append(ss)
                flag=False

        if complete:
            answer.append(complete)

    return answer


# 리스트를 이용한 타인 풀이(올림 이용)

# def solution(progresses, speeds):
#     Q=[]
#     for p, s in zip(progresses, speeds):
#         if len(Q)==0 or Q[-1][0]<-((p-100)//s):
#             Q.append([-((p-100)//s),1])
#         else:
#             Q[-1][1]+=1
#     return [q[1] for q in Q]