# 등굣길

# dfs와 dp를 이용한 풀이
# https://programmers.co.kr/learn/courses/30/lessons/42898

dx=[0,1]
dy=[1,0]

def dfs(x,y,puddles,m,n):
    if x==n-1 and y==m-1:
        return 1

    if dp[x][y]==-1:
        dp[x][y]=0
        for i in range(2):
            nx=x+dx[i]
            ny=y+dy[i]
            if 0<=nx<n and 0<=ny<m:
                if [ny+1,nx+1] not in puddles:
                    dp[x][y]+=dfs(nx,ny,puddles,m,n)

    return dp[x][y]

def solution(m, n, puddles):
    global dp
    dp=[[-1 for _ in range(m)] for _ in range(n)]

    return dfs(0,0,puddles,m,n)%1000000007

# 함수 안의 함수 / dictionary 를 이용한 타인 풀이
# def solution(m, n, puddles):
#     answer = 0
#     info = dict([((2, 1), 1), ((1, 2), 1)])
#     for puddle in puddles:
#         info[tuple(puddle)] = 0
#
#     def func(m, n):
#         if m < 1 or n < 1:
#             return 0
#         if (m, n) in info:
#             return info[(m, n)]
#         return info.setdefault((m, n), func(m - 1, n) + func(m, n - 1))
#     return  func(m, n) % 1000000007