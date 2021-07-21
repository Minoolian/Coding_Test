# 단속카메라

# 정렬을 이용한 풀이
# https://programmers.co.kr/learn/courses/30/lessons/42884

def solution(routes):
    answer = 0
    routes.sort()
    s,e=routes[0][0],routes[0][1]

    for ss,ee in routes[1:]:
        if e<ss:
            answer+=1
            s,e=ss,ee
            continue
        if s<ss: s=ss
        if e>ee: e=ee

    return answer