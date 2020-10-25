# 격자판의 숫자 이어 붙이기

# DFS를 이용한 풀이
# https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV7I5fgqEogDFAXB&categoryId=AV7I5fgqEogDFAXB&categoryType=CODE

t=int(input())

def dfs(x, y, l, s):
    s+=lis[x][y]
    if not l:
        result.add(s)
        return

    idx_x=[1,0,-1,0]
    idx_y=[0,1,0,-1]

    # visit[x][y]=1
    for i in range(4):
        n_x=x+idx_x[i]
        n_y=y+idx_y[i]
        if (n_x<4 and n_x>=0) and (n_y<4 and n_y>=0):
            # if not visit[n_x][n_y]:
                dfs(n_x, n_y, l-1,s)
    # visit[x][y]=0

for tc in range(1, t+1):
    lis=[list(map(str,input().split())) for _ in range(4)]
    result=set()
    for i in range(4):
        for j in range(4):
            # visit=[[0]*4 for _ in range(4)]
            dfs(i,j,6,"")

    print("#{} {}".format(tc, len(result)))
