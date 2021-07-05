# H-Index

# 명시된 정의를 이용한 풀이
# https://programmers.co.kr/learn/courses/30/lessons/42747

def solution(citations):
    answer=len(citations)
    citations.sort(reverse=True)

    for i in range(len(citations)):
        if citations[i]<i+1:
            answer=i
            break

    return answer

assert solution([3,0,6,1,5])==3