# 테트로미노

#
# https://www.acmicpc.net/problem/14500

dx=[-1,0,1,0]
dy=[0,1,0,-1]

def dfs(x,y,l,s):
    global result
    if result>=s+high*(4-l):
        return
    if l==4:
        result=max(result,s)
        return
    else:
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if 0<=nx<n and 0<=ny<m and visit[nx][ny]:
                if l==2:
                    visit[nx][ny]=False
                    dfs(x,y,l+1,s+tetro[nx][ny])
                    visit[nx][ny]=True

                visit[nx][ny]=False
                dfs(nx,ny,l+1,s+tetro[nx][ny])
                visit[nx][ny]=True

n,m=map(int,input().split())
tetro=[list(map(int,input().split())) for _ in range(n)]
visit=[[True]*m for _ in range(n)]
high=max(map(max,tetro))

result=0
for i in range(n):
    for j in range(m):
        visit[i][j]=False
        dfs(i,j,1,tetro[i][j])
        visit[i][j]=True

print(result)

