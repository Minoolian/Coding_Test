# 큰 수 만들기

# 반복문을 이용한 풀이
# https://programmers.co.kr/learn/courses/30/lessons/42883?language=python3

def solution(number, k):
    answer=''
    idx=0

    for i in range(len(number)-k):
        max=0
        for j in range(idx,i+k+1):
            if max<number[j]:
                idx=j+1
                max=number[j]

        answer.append(max)

    return answer

# 시간초과
# from itertools import combinations
#
# def solution(number, k):
#
#     return str(max([''.join(map(lambda x:number[x],s)) for s in combinations(range(len(number)),len(number)-k)]))
