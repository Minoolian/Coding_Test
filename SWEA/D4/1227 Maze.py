# 미로2

# BFS를 이용한 풀이
# https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=3&problemLevel=4&problemLevel=5&contestProbId=AV14wL9KAGkCFAYD&categoryId=AV14wL9KAGkCFAYD&categoryType=CODE&problemTitle=&orderBy=RECOMMEND_COUNT&selectCodeLang=PYTHON&select-1=5&pageSize=30&pageIndex=2

from collections import deque

idx_x=[0,1,0,-1]
idx_y=[1,0,-1,0]

for tc in range(1, 11):
    n=int(input())

    maze=[]
    q=deque()
    visit=[[True]*100 for _ in range(100)]

    for i in range(100):
        l=str(input())
        if '2' in l:
            for j in range(100):
                if l[j]=='2':
                    q.append((i,j))
                    visit[i][j]=False
        maze.append(l)

    result=0
    while q:
        x,y=q.popleft()

        for i in range(4):
            nx=x+idx_x[i]
            ny=y+idx_y[i]

            if maze[nx][ny]=='3':
                result=1
                break

            if visit[nx][ny] and maze[nx][ny]=='0' and 0<=nx<100 and 0<=ny<100:
                q.append((nx,ny))
                visit[nx][ny]=False

    print(f"#{tc} {result}")
