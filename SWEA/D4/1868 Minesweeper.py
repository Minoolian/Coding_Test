# 파핑파핑 지뢰찾기

# DFS를 이용한 풀이.
# https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV5LwsHaD1MDFAXc&categoryId=AV5LwsHaD1MDFAXc&categoryType=CODE

from collections import deque

def dfs(x, y):

    for i in range(8):
        nx=x+idx_x[i]
        ny=y+idx_y[i]
        if nx>=0 and nx<n and ny>=0 and ny<n:
            if visit[nx][ny] and conv[nx][ny]>0:
                visit[nx][ny]=False
            elif visit[nx][ny] and conv[nx][ny]==0:
                visit[nx][ny]=False
                dfs(nx, ny)



if __name__=="__main__":
    idx_x=[1,0,-1,0,1,-1,1,-1]
    idx_y=[0,1,0,-1,1,-1,-1,1]

    t=int(input())

    for tc in range(1, t+1):
        n=int(input())
        lis=[list(map(str,input())) for _ in range(n)]
        conv=[[None]*n for _ in range(n)]
        visit=[[True]*n for _ in range(n)]
        q=deque()

        for x in range(n):
            for y in range(n):
                m=0
                if lis[x][y]=='*':
                    conv[x][y]=-1
                    visit[x][y]=False
                    continue

                for i in range(8):
                    nx=x+idx_x[i]
                    ny=y+idx_y[i]

                    if nx>=0 and nx<n and ny>=0 and ny<n:
                        if lis[nx][ny]=='*':
                            m+=1

                conv[x][y]=m

        fin=0
        for x in range(n):
            for y in range(n):
                if conv[x][y]==0 and visit[x][y]:
                    fin+=1
                    visit[x][y]=False
                    dfs(x,y)

        for x in range(n):
            for y in range(n):
                if visit[x][y]:
                    fin+=1

        print("#{} {}".format(tc,fin))

