# 내리막 길

# 지도가 주어질 때 제일 왼쪽 위 지점에서 출발하여 제일 오른쪽 아래 지점까지 항상 내리막길로만 이동하는 경로의 개수를 구하는 프로그램.

import sys
sys.setrecursionlimit(10000) # 파이썬이 재귀 깊이를 작게 설정하기에 높여준다.

dx=[1,-1,0,0]
dy=[0,0,1,-1]

def dfs(x, y):
    if x==0 and y==0: # 최종 목적지에 다다르면 1을 리턴
        return 1 # 1로 체크된 값을 만난다면 이미 존재하는 경로라는 것을 암시하고 DFS를 수행하지 않는다.

    if dp[x][y]==-1:
        dp[x][y]=0 # 경로를 사용했다는 표시
        for i in range(4): # 4방향 모두 확인
            nx=x+dx[i]
            ny=y+dy[i]
            if 0<=nx<m and 0<=ny<n:
                if lis[x][y] < lis[nx][ny]: # 해당 경로를 갈 수 있으면
                    dp[x][y]+=dfs(nx,ny) # 수를 추가
    return dp[x][y]

m,n = map(int,sys.stdin.readline().split())
lis=[list(map(int,sys.stdin.readline().split())) for _ in range(m)]
dp=[[-1]*n for _ in range(m)]
print(dfs(m-1,n-1))

