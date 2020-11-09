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
    p=["Bob","Alice"]
    loser=0

    # dfs(1, 1)
    depth=math.ceil(math.log(m,2))
    result=1
    for i in range(1, depth):
        if i%2:
            result=result*2+1
        else:
            result=result*2

    if result>m:
        if depth%2: idx=1
        else: idx=0
    else:
        if depth%2: idx=1
        else: idx=0

    print("#{} {}".format(tc,p[idx]))