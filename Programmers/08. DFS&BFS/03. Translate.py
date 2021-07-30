# 단어 변환

# BFS를 이용한 풀이
# https://programmers.co.kr/learn/courses/30/lessons/43163

from collections import deque

def solution(begin, target, words):

    if target not in words:
        return 0

    visit={w:True for w in words}
    q=deque([[0,begin]])

    while q:
        l,w=q.popleft()
        if w==target:
            return l

        for ww in words:
            if visit[ww] and len([True for x,y in zip(w,ww) if x!=y])==1:
                visit[ww]=False
                q.append([l+1,ww])

    return 0

# 제너레이터를 이용한 타인풀이
# from collections import deque
# 
# def get_adjacent(current, words):
#     for word in words:
#         if len(current) != len(word):
#             continue
# 
#         count = 0
#         for c, w in zip(current, word):
#             if c != w:
#                 count += 1
# 
#         if count == 1:
#             yield word
# 
# 
# def solution(begin, target, words):
#     dist = {begin: 0}
#     queue = deque([begin])
# 
#     while queue:
#         current = queue.popleft()
# 
#         for next_word in get_adjacent(current, words):
#             if next_word not in dist:
#                 dist[next_word] = dist[current] + 1
#                 queue.append(next_word)
# 
#     return dist.get(target, 0)