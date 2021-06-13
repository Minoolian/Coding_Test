# 위장

# Dictionary를 이용한 풀이
# https://programmers.co.kr/learn/courses/30/lessons/42578

def solution(clothes):
    answer = 1
    comb={}

    for cloth, var in clothes:
        comb[var]=1 if var not in comb else comb[var]+1

    for x in comb.values():
        answer*=(x+1)


    return answer-1


# reduce 함수를 이용한 풀이 (누적을 구하는 함수)

# import collections
# from functools import reduce
#
# def solution(c):
#     return reduce(lambda x,y:x*y,[a+1 for a in collections.Counter([x[1] for x in c]).values()])-1