# 파핑파핑 지뢰찾기

#
# https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV5LwsHaD1MDFAXc&categoryId=AV5LwsHaD1MDFAXc&categoryType=CODE

from collections import deque

n=int(input())
lis=[list(map(str,input())) for _ in range(n)]
mine=[[None]*n for _ in range(n)]
visit=[[True]*n for _ in range(n)]

def bfs():

    q=deque()

    q.append([0,0])

    while q:
        x,y=q.popleft()

        m=0
        for i in range(8):
            nx=x+idx_x[i]
            ny=y+idx_y[i]

            if lis[nx][ny]=='*':
                m+=1
            if visit[nx][ny] and lis[nx][ny]!='*':
                visit[nx][ny]=False
                q.append([nx,ny])

        



idx_x=[1,0,-1,0,1,-1,1,-1]
idx_y=[0,1,0,-1,1,-1,-1,1]

# def dfs(x,y):
#     m=0
#     for i in range(8):
#         nx=x+idx_x[i]
#         ny=y+idx_y[i]
#         if lis[nx][ny]=='*':
#             m+=1
#     mine[x][y]=m
#     visit[x][y]=False
#
#     if m==0:
#         for i in range(4):
#             nx=x+idx_x[i]
#             ny=y+idx_y[i]
#             if visit[nx][ny]:
#                 dfs(nx,ny)
#
#     if not visit[x][y]:
#
#
