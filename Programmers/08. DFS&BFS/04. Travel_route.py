# 여행경로

#
# https://programmers.co.kr/learn/courses/30/lessons/43164
from collections import defaultdict

def solution(tickets):
    answer=[]
    tks=defaultdict(list)

    for k,v in sorted(tickets):
        tks[k]= tks[k]+[v] if k in tks else [v]

    def dfs(cur):
        while tks[cur]:
            dfs(tks[cur].pop(0))
        answer.append(cur)
    dfs('ICN')

    return answer[::-1]


# def dfs(l,dep,cur,tks):
#     if l==dep:
#         return [cur]
#
#     for i in range(len(tks[cur])):
#         next=tks[cur][i]
#         result=dfs(l+1,dep,next,tks)
#         if temp[0]>result[0]:
#             temp=result
#         tks[cur].append(next)
#
#     if len(result):
#         return [cur]+result
#
# def solution(tickets):
#     tks={}
#     for k,v in tickets:
#         tks[k]= sorted(tks[k]+[v]) if k in tks else [v]
#
#     print(tks)

print(solution([["ICN", "JFK"], ["HND", "IAD"], ["JFK", "HND"]]))
