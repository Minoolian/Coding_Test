# 소수 찾기

# 에라토스테네스의 체를 이용한 풀이
# https://programmers.co.kr/learn/courses/30/lessons/42839

from itertools import permutations

def solution(numbers):
    answer = 0

    era=[False,False]+[True for _ in range(9999998)]

    for i in range(2,int(10000000**0.5)+1):
        if era[i]:
            for j in range(i+i, 10000000, i):
                era[j]=False

    num=[i for j in range(1,len(numbers)+1) for i in permutations(numbers,j)]
    for check in set([int(''.join(map(str,n))) for n in num]):
        if era[check]:
            answer+=1

    return answer

# Set을 이용한 에라토스테네스의 체 이용 (타인풀이)
# from itertools import permutations
# def solution(n):
#     a = set()
#     for i in range(len(n)):
#         a |= set(map(int, map("".join, permutations(list(n), i + 1))))
#     a -= set(range(0, 2))
#     for i in range(2, int(max(a) ** 0.5) + 1):
#         a -= set(range(i * 2, max(a) + 1, i))
#     return len(a)