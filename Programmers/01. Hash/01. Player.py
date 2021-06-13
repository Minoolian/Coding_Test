# 완주하지 못한 선수

# Dictionary를 이용한 풀이
# https://programmers.co.kr/learn/courses/30/lessons/42576

from collections import Counter

def solution(participant, completion):
    answer = ''
    check=Counter(participant)

    for p in completion:
        check[p]-=1
        if not check[p]: check.pop(p)

    return ''.join(check.keys())


# 고유 해시값을 이용한 타인풀이

# def solution(participant, completion):
#     answer = ''
#     temp = 0
#     dic = {}
#     for part in participant:
#         dic[hash(part)] = part
#         temp += int(hash(part))
#     for com in completion:
#         temp -= hash(com)
#     answer = dic[temp]
#
#     return answer