# 소가 길을 건너간 이유6

#
# https://www.acmicpc.net/problem/14466

n,k,r=map(int,input().split())
road=set()
for _ in range(r):
    r,c,rr,cc=map(int,input().split())
    road.add((r-1,c-1,rr-1,cc-1))
    road.add((rr-1,cc-1,r-1,c-1))

cow=[]
for _ in range(k):
    r,c=map(int,input().split())
    cow.append([r-1,c-1])

farm=[[1 if [i,j] in cow else 0 for j in range(n)] for i in range(n)]

dx=[1,0,-1,0]
dy=[0,1,0,-1]

answer=0
for r,c in cow:
    farm[r][c]=0
    q=[[r,c]]
    visit=[[True]*n for _ in range(n)]
    visit[r][c]=False

    meet=0
    while q:
        x,y=q.pop(0)

        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]

            if 0<=nx<n and 0<=ny<n and visit[nx][ny] and (x,y,nx,ny) not in road:
                if farm[nx][ny]:
                    meet+=1
                visit[nx][ny]=False
                q.append([nx,ny])

    answer+=k-meet-1
    k-=1

print(answer)