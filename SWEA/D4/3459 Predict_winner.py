# 승자 예측하기

#
# https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AWFPoj1qANoDFAV0&categoryId=AWFPoj1qANoDFAV0&categoryType=CODE


# DFS 풀이 시간초과
# def dfs(turn, x):
#     global loser
#
#     if x>m:
#         return True
#
#     A=dfs(turn+1, (2*x)+1)
#     B=dfs(turn+1, 2*x)
#
#     if A and B:
#         loser=max(loser,turn)
#
#     return False

import math

t=int(input())
for tc in range(1, t+1):
    m=int(input())
    loser=0

    # dfs(1, 1)
    depth=int(math.log(m,2))+1
    result=1
    if depth%2:
        for i in range(1, depth):
            if i%2:
                result=result*2+1
            else:
                result=result*2
    else:
        for i in range(1, depth):
            if i%2:
                result=result*2
            else:
                result=result*2+1

    if depth%2:
        if result>m: winner="Alice"
        else: winner="Bob"
    else:
        if result>m: winner="Bob"
        else: winner="Alice"

    print("#{} {}".format(tc,winner))