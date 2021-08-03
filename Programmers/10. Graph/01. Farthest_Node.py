# 가장 먼 노드

#
# https://programmers.co.kr/learn/courses/30/lessons/49189

from collections import deque

def solution(n, edge):
    answer = 0
    matrix=[[] for _ in range(n+1)]
    visit=[True for _ in range(n+1)]
    for u,v in edge:
        matrix[u].append(v)
        matrix[v].append(u)

    max_depth=0
    q=deque([[0,1]])
    visit[1]=False
    
    while q:
        depth,n=q.popleft()

        if max_depth<depth:
            max_depth=depth
            answer=1
        elif max_depth==depth:
            answer+=1

        for next in matrix[n]:
            if visit[next]:
                q.append([depth+1,next])
                visit[next]=False
    
    return answer

print(solution(6,[[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]))