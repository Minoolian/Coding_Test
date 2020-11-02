# 파핑파핑 지뢰찾기

#
# https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV5LwsHaD1MDFAXc&categoryId=AV5LwsHaD1MDFAXc&categoryType=CODE

from collections import deque

def bfs():
    q=deque()
    result=0

    for i in range(n):
        for j in range(n):
            
            if visit[i][j] and conv[i][j]!=-1:
                q.append([i,j])
                while q:
                    x,y=q.popleft()

                    if conv[x][y]!=-1 and visit[x][y]:
                        visit[x][y]=False

                        if conv[x][y]==0:
                            for k in range(8):
                                nx=x+idx_x[k]
                                ny=y+idx_y[k]
                                if nx>=0 and nx<n and ny>=0 and ny<n:
                                    q.append([nx,ny])
                        else:
                            for k in range(8):
                                nx=x+idx_x[k]
                                ny=y+idx_y[k]
                                if nx>=0 and nx<n and ny>=0 and ny<n and conv[nx][ny]==0 and visit[nx][ny]:
                                    q.append([nx,ny])

                result+=1

    return result


if __name__=="__main__":
    idx_x=[1,0,-1,0,1,-1,1,-1]
    idx_y=[0,1,0,-1,1,-1,-1,1]

    t=int(input())

    for tc in range(1, t+1):
        n=int(input())
        lis=[list(map(str,input())) for _ in range(n)]
        conv=[[None]*n for _ in range(n)]

        mine=[[None]*n for _ in range(n)]
        visit=[[True]*n for _ in range(n)]

        for x in range(n):
            for y in range(n):
                m=0
                if lis[x][y]=='*':
                    conv[x][y]=-1
                    continue

                for i in range(8):
                    nx=x+idx_x[i]
                    ny=y+idx_y[i]

                    if nx>=0 and nx<n and ny>=0 and ny<n:
                        if lis[nx][ny]=='*':
                            m+=1

                conv[x][y]=m

        print("#{} {}".format(tc,bfs()))

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
