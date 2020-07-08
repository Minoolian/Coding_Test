# 단지번호 붙이기

# 1은 집이 있는 곳을, 0은 집이 없는 곳을 나타낸다
# 연결되었다는 것은 어떤 집이 좌우, 혹은 아래위로 다른 집이 있는 경우를 말한다. 대각선상에 집이 있는 경우는 연결된 것이 아니다
# 첫 번째 줄에는 총 단지수를 출력하시오. 그리고 각 단지내 집의 수를 오름차순으로 정렬하여 한 줄에 하나씩 출력

import sys

n=int(sys.stdin.readline())
lis=[sys.stdin.readline().rstrip() for _ in range(n)]
visit=[[0]*n for _ in range(n)]

total=0 # 총 단지의 수를 담는 값

vec_x = [-1, 0, 1, 0] # 상하좌우를 이동할 vector
vec_y = [0, 1, 0, -1]

result=[] # 매 단지의 집의 수를 담는 리스트


def dfs(x, y): 
    global count

    visit[x][y]=1
    count+=1


    for i in range(4):
        nx=x+vec_x[i]
        ny=y+vec_y[i]
        if nx<0 or nx>=n or ny<0 or ny>=n:
            continue

        if visit[nx][ny]==0 and lis[nx][ny]=='1':
            dfs(nx,ny)


for i in range(n): # 모든 집을 순환하면서 확인
    for j in range(n):
        if visit[i][j]==0 and lis[i][j]=='1':
            count=0
            dfs(i,j)
            result.append(count)
            total+=1

print(total)
result.sort()
for i in result:
    print(i)



