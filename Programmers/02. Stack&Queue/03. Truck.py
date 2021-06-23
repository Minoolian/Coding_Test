# 다리를 지나는 트럭

# 큐를 이용한 풀이
# https://programmers.co.kr/learn/courses/30/lessons/42583

from collections import deque

def solution(bridge_length, weight, truck_weights):
    answer = 0

    truck=deque(truck_weights)
    q=deque()

    length=0
    while truck:
        if weight>=truck[0] and length!=bridge_length:
            weight-=truck[0]
            for i in range(len(q)):
                q[i][1]+=1

            q.append([truck.popleft(),1])
            length=q[0][1]
            answer+=1

        else:
            w,t=q.popleft()
            nt=bridge_length-t
            weight+=w
            answer+=nt

            for i in range(len(q)):
                q[i][1]+=nt
            if q:
                length=q[0][1]

    w,t=q.pop()
    answer+=bridge_length-t+1

    return answer

print(solution(5, 5, [2,2,2,2,1,1,1,1,1]))