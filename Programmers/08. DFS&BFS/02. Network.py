# 네트워크

# BFS를 이용한 풀이
# https://programmers.co.kr/learn/courses/30/lessons/43162

from collections import deque


def solution(n, computers):
    answer=0
    v={i for i in range(n)}
    q=deque()

    while v:
        q.append(v.pop())
        answer+=1
        while q:
            u=q.popleft()
            # map(lambda x:q.append(x),[i for i,v in enumerate(computers[u]) if v])
            for i,u in enumerate(computers[u]):
                if u and i in v:
                    q.append(i)
                    v.remove(i)

    return answer

print(solution(3,[[1, 1, 0], [1, 1, 1], [0, 1, 1]]))