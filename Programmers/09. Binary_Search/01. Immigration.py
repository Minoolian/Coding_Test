# 입국심사

# 이진탐색을 이용한 풀이
# https://programmers.co.kr/learn/courses/30/lessons/43238

def solution(n, times):
    left,right=0,times[-1]*n

    while left<right:
        mid=(left+right)//2
        nn=sum(map(lambda x:mid//x,times))

        if nn>=n: right=mid
        else: left=mid+1

    return left


# 시간초과 & 틀린풀이
# from bisect import bisect_left
#
# def solution(n, times):
#     times.sort()
#     answer=[]
#
#     i=1
#     while len(answer)<=n:
#         for value in times:
#             k=bisect_left(answer, value*i)
#             if len(answer)<=k:
#                 answer.append(value*i)
#             else:
#                 answer=answer[:k]+[value*i]+answer[k:]
#         i+=1
#
#     return answer[n-1]

print(solution(6, [7,10]))

