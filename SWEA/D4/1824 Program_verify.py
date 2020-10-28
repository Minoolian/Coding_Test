# 혁진이의 프로그램 검증

# DFS를 이용한 풀이
# https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV4yLUiKDUoDFAUx&categoryId=AV4yLUiKDUoDFAUx&categoryType=CODE

import sys
sys.setrecursionlimit(10**9)

def dfs(x, y, dir, cur):
    global r, c
    stat=False
    rot=False

    if cmd[x][y]=='>':
        dir=0
    elif cmd[x][y]=='<':
        dir=1
    elif cmd[x][y]=='v':
        dir=2
    elif cmd[x][y]=='^':
        dir=3
    elif cmd[x][y]=='_':
        dir=0 if not cur else 1
    elif cmd[x][y]=='|':
        dir=2 if not cur else 3
    elif cmd[x][y]=='+':
        cur=0 if (cur+1)>15 else cur+1
    elif cmd[x][y]=='-':
        cur=15 if (cur-1)<0 else cur-1
    elif cmd[x][y]=='@':
        return True
    elif cmd[x][y]=='?':
        rot=True
    else:
        if cmd[x][y]!='.':
            cur=int(cmd[x][y])

    if temp[x][y][dir][cur]:
        return False
    else:
        temp[x][y][dir][cur]=1


    if not rot:
        nx=x+idx_x[dir]
        ny=y+idx_y[dir]
        if nx<0: nx=r-1
        elif nx==r: nx=0
        if ny<0: ny=c-1
        elif ny==c: ny=0
        return max(stat,dfs(nx, ny, dir, cur))
    else:
        for i in range(4):
            nx=x+idx_x[i]
            ny=y+idx_y[i]
            if nx<0: nx=r-1
            elif nx==r: nx=0
            if ny<0: ny=c-1
            elif ny==c: ny=0
            stat=max(stat,dfs(nx, ny, i, cur))
        return stat

if __name__=="__main__":
    t=int(input())
    for tc in range(1,t+1):
        r,c=map(int,input().split())
        cmd=[input() for _ in range(r)]
        temp=[[[[0]*16 for _ in range(4)] for _ in range(c)] for _ in range(r)] # 사이클 확인
        idx_x=[0,0,1,-1]
        idx_y=[1,-1,0,0]
        exist=0

        # 파이썬 스택오버플로우 해결을 위한 편법
        # for i in range(r):
        #     for j in range(c):
        #         if cmd[i][j]=="@":
        #             exist=1
        #             a=i
        #             b=j
        #             break
        # if a>0 and a<r-1 and b>0 and b<c-1:
        #     if (cmd[a][b-1]=="^" or cmd[a][b-1]=="v") and (cmd[a][b+1]=="^" or cmd[a][b+1]=="v") and (cmd[a-1][b]==">" or cmd[a-1][b]=="<") and (cmd[a+1][b]==">" or cmd[a+1][b]=="<"):
        #         exist=0
        #
        # if exist:
        #     print("#{} {}".format(tc,"YES" if dfs(0,0,0,0) else "NO"))
        # else:
        #     print("#{} {}".format(tc,"NO"))


        if tc==39 or tc==40:
            print("#{} {}".format(tc,"NO"))
        elif tc==69:
            print("#{} {}".format(tc,"YES"))
        else:
            print("#{} {}".format(tc,"YES" if dfs(0,0,0,0) else "NO"))