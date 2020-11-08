# 미로1

#
# https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV14vXUqAGMCFAYD&categoryId=AV14vXUqAGMCFAYD&categoryType=CODE

def dfs(x, y):
    if maze[x][y]==3:
        return True

    if not visit[x][y] or maze[x][y]==1:
        return

    visit[x][y]=False
    for i in range(4):
        nx=x+idx_x[i]
        ny=y+idx_y[i]

        if dfs(nx, ny):
            return True

for tc in range(1, 11):
    n=int(input())
    maze=[list(map(int,input())) for _ in range(16)]
    visit=[[True]*16 for _ in range(16)]
    idx_x=[1,0,-1,0]
    idx_y=[0,1,0,-1]
    flag=0

    for i in range(16):
        for j in range(16):
            if maze[i][j]==2:
                flag=1
                break
        if flag:
            break

    if dfs(i,j):
        print("#{} {}".format(tc,1))
    else:
        print("#{} {}".format(tc,0))

