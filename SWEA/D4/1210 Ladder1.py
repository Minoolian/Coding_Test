# Ladder1

# DFS를 이용한 풀이
# https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV14ABYKADACFAYh&categoryId=AV14ABYKADACFAYh&categoryType=CODE

def dfs(x, y, dir):
    if x==99:
        if maze[x][y]==2:
            return True
        else:
            return False

    if dir:
        if dir==1 and y+1<100 and maze[x][y+1]:
            y=y+1
        elif dir==2 and y-1>=0 and maze[x][y-1]:
            y=y-1
        else:
            x=x+1
            dir=0

        result=dfs(x,y,dir)
        return result

    else:
        if y+1<100 and maze[x][y+1]:
            dir=1
            y=y+1
        elif y-1>=0 and maze[x][y-1]:
            dir=2
            y=y-1
        else:
            x=x+1
        result=dfs(x,y,dir)
        return result

for _ in range(10):
    tc=int(input())
    maze=[list(map(int,input().split())) for _ in range(100)]

    for i in range(100):
        if maze[0][i]:
            if dfs(0,i,0):
                print("#{} {}".format(tc,i))
                break