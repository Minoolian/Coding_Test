# 지희의 고장난 계산기

#
# https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV4yC3pqCegDFAUx&categoryId=AV4yC3pqCegDFAUx&categoryType=CODE

#

def bfs():


tmp=list(map(int,input().split()))
calc=[]
for i in range(len(tmp)):
    if tmp[i]:
        calc.append(i)

fin=int(input())

# 잘못 접근한 방법 ( 수 X 수 로만 가는 방향)
# import sys
# sys.setrecursionlimit(10**9)
# from itertools import permutations
#
# def check():
#     for n in list(str(fin)):
#         if int(n) not in calc:
#             return True
#
#     return False
#
# def dfs(left, right, op):
#     global result
#
#     if left*right>int(fin):
#         return
#
#     if left*right==int(fin):
#         result=min(result,op)
#         return
#
#     for i in calc:
#         dfs(left*10+i,right,op+1)
#         dfs(left,right*10+i,op+1)
#
# t=int(input())
# for tc in range(1,t+1):
#     tmp=list(map(int,input().split()))
#     calc=[]
#     for i in range(len(tmp)):
#         if tmp[i]:
#             calc.append(i)
#
#     fin=input()
#     result=float('inf')
#
#     if check():
#         p=permutations(calc,2)
#         for a,b in p:
#             dfs(a, b, 2)
#         if result==float('inf'):
#             result=-1
#         else:
#             result+=2
#     else:
#         result=len(fin)+1
#
#
#     print(result)
