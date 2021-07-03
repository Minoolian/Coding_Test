# K번째 수

# 단순 정렬을 이용한 풀이
# https://programmers.co.kr/learn/courses/30/lessons/42748

def solution(array, commands):
    return [sorted(array[i-1:j])[k-1] for i,j,k in commands]

solution([1, 5, 2, 6, 3, 7, 4],[[2, 5, 3], [4, 4, 1], [1, 7, 3]])