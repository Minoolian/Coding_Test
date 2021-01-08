# 새샘이의 7-3-5 게임

# DFS, 모듈을 이용한 풀이
# https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AWZ2IErKCwUDFAUQ&categoryId=AWZ2IErKCwUDFAUQ&categoryType=CODE

# DFS를 이용한 방법
# def dfs(n,cnt,visit):
#     global result
#
#     if cnt==3:
#         result.append(n)
#         return
#
#     for i in range(len(lis)):
#         if visit[i]:
#             visit[i]=False
#             dfs(n+lis[i],cnt+1,visit)
#             visit[i]=True
#
#
# t=int(input())
# for tc in range(1, t+1):
#     result=[]
#     lis=list(map(int,input().split()))
#     visit=[True for _ in range(len(lis))]
#
#     dfs(0, 0, visit)
#     result=list(set(result))
#     result.sort()
#     print(f"#{tc} {result[-5]}")


from itertools import combinations

t=int(input())
for tc in range(1, t+1):
    lis=list(map(int,input().split()))

    result=[]
    for i in combinations(lis,3):
        result.append(sum(i))

    result=list(set(result))
    result.sort()
    print(f"#{tc} {result[-5]}")