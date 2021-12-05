# Island Travels

# BFS와 비트마스크를 이용한 풀이
# https://www.acmicpc.net/problem/5852

from collections import deque
import heapq as hq

dx=[1,0,-1,0]
dy=[0,1,0,-1]

def check_island(x,y,num):
    if island[x][y]!=0 or squares[x][y]!='X': return

    island[x][y]=num
    for i in range(4):
        nx=x+dx[i]
        ny=y+dy[i]

        if 0<=nx<r and 0<=ny<c:
            check_island(nx, ny, num)

def bfs(i,j,cur):
    visited=[[False]*c for _ in range(r)]
    check=[[float('inf')]*c for _ in range(r)]
    q=[]
    hq.heappush(q, [0,i,j])

    while q:
        cost,x,y=hq.heappop(q)
        if visited[x][y] and check[x][y]<=cost: continue
        if island[x][y]>0:
            distance[cur][island[x][y]]=min(cost, distance[cur][island[x][y]])
        visited[x][y]=True
        check[x][y]=cost

        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if 0<=nx<r and 0<=ny<c and squares[nx][ny]!='.':
                ncost=cost
                if squares[nx][ny]=='S':
                    ncost+=1
                hq.heappush(q, [ncost, nx, ny])


    # visited=[[True]*c for _ in range(r)]
    # visited_island=[False]*num
    # q=deque()
    # q.append([0,i,j])
    # visited[i][j]=False
    # visited_island[cur]=True
    #
    # while q:
    #     cost, x, y=q.popleft()
    #
    #     if squares[x][y]=='X' and island[x][y]!=cur:
    #         distance[cur][island[x][y]]=min(distance[cur][island[x][y]], cost)
    #         # visited_island[island[x][y]]=True
    #         # if all(visited_island[1:]):
    #         #     break
    #
    #     for i in range(4):
    #         nx=x+dx[i]
    #         ny=y+dy[i]
    #
    #         if 0<=nx<r and 0<=ny<c and squares[nx][ny]!='.' and visited[nx][ny]:
    #             visited[nx][ny]=False
    #             if squares[nx][ny]=='S':
    #                 q.append([cost+1, nx, ny])
    #             elif squares[nx][ny]=='X':
    #                 q.append([cost, nx, ny])

def swim(visit, idx):
    if dp[visit][idx]:
        return dp[visit][idx]

    if visit==(1<<num)-2:
        dp[visit][idx]=0
        return dp[visit][idx]

    tmp=float('inf')
    for next in range(1, num):
        if idx==next or (visit & (1<<next)): continue
        tmp=min(tmp,swim((visit | (1<<next)), next)+distance[idx][next])

    dp[visit][idx]=tmp
    return tmp


r,c=map(int,input().split())
squares=[input() for _ in range(r)]
island=[[0]*c for _ in range(r)]

num=1
for i in range(r):
    for j in range(c):
        if squares[i][j]=='X' and island[i][j]==0:
            check_island(i,j,num)
            num+=1

distance=[[0 if i==0 or j==0 else float('inf') for i in range(num)] for j in range(num)]
visit=[True]*num
for i in range(r):
    for j in range(c):
        if squares[i][j]=='X' and visit[island[i][j]]:
            visit[island[i][j]]=False
            bfs(i,j,island[i][j])

dp=[[0]*17 for _ in range(1<<17)]
print(swim(0,0))

# 다익스트라로 수정