# 징검다리

# 이분탐색을 이용한 풀이
# https://programmers.co.kr/learn/courses/30/lessons/43236

def solution(distance, rocks, n):
    answer = 0
    left, right=1, distance
    rocks.sort()

    while left<=right:
        mid=(left+right)//2

        pre=0
        delete=0
        for r in rocks:
            if r-pre<mid:
                delete+=1
            else:
                pre=r

            if delete>n:
                break

        if delete>n:
            right=mid-1
        elif delete<=n:
            answer=mid
            left=mid+1
    return answer

print(solution(25,[2, 14, 11, 21, 17],2))
