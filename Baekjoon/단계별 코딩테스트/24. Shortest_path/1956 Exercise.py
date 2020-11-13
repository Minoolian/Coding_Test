# 운동

# V개의 마을와 E개의 도로로 구성되어 있는 도시
# 사이클을 이루는 도로의 길이의 합이 최소가 되도록 찾으려고 한다.

# 플로이드-워셜 알고리즘으로 모든 최단경로를 구한 후
# 자기자신으로 돌아오는 최단거리들 중 최소를 출력

import sys

inf=sys.maxsize

v, e=map(int,sys.stdin.readline().split())
dp=[[inf]*(v) for _ in range(v)] # 인접행렬 생성

def floyd(): # O(V^3)의 시간복잡도.
    for k in range(v):
        for i in range(v):
            for j in range(v):
                if dp[i][j] > dp[i][k]+dp[k][j]:
                    dp[i][j] = dp[i][k]+dp[k][j]

for _ in range(e):
    a,b,c=map(int,sys.stdin.readline().split())
    dp[a-1][b-1]=c

floyd()
result=inf
for i in range(v):
    result=min(result,dp[i][i])

if result == inf:
    print(-1)
else:
    print(result)