# Ladder2

# DFS를 이용한 풀이
# https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV14BgD6AEECFAYh&categoryId=AV14BgD6AEECFAYh&categoryType=CODE

def dfs(x, y, dir):
    if x==99:
        return 1

    if dir:
        if dir==1 and y+1<100 and maze[x][y+1]:
            y=y+1
        elif dir==2 and y-1>=0 and maze[x][y-1]:
            y=y-1
        else:
            x=x+1
            dir=0


        return dfs(x,y,dir)+1

    else:
        if y+1<100 and maze[x][y+1]:
            dir=1
            y=y+1
        elif y-1>=0 and maze[x][y-1]:
            dir=2
            y=y-1
        else:
            x=x+1

        return dfs(x,y,dir)+1

for _ in range(10):
    tc=int(input())
    maze=[list(map(int,input().split())) for _ in range(100)]
    path=float('inf')

    for i in range(100):
        if maze[0][i]:
            result=dfs(0,i,0)
            if path>result:
                path=result
                idx=i


    print("#{} {}".format(tc,idx))
