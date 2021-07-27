# 타겟 넘버

#
# https://programmers.co.kr/learn/courses/30/lessons/43165

def solution(numbers, target):
    answer = 0

    def dfs(i=0, result=0):
        nonlocal answer

        if i==len(numbers):
            if target==result:
                answer+=1
            return
        dfs(i+1,result+numbers[0])
        dfs(i+1,result-numbers[0])

    dfs()
    return answer

# solution 자체를 이용한 타인 풀이
# def solution(numbers, target):
#     if not numbers and target == 0 :
#         return 1
#     elif not numbers:
#         return 0
#     else:
#         return solution(numbers[1:], target-numbers[0]) + solution(numbers[1:], target+numbers[0])


# 카타시안 곱을 이용한 타인 풀이
# from itertools import product
# def solution(numbers, target):
#     l = [(x, -x) for x in numbers]
#     s = list(map(sum, product(*l)))
#     return s.count(target)