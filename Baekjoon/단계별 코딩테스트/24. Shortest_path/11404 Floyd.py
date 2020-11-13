# 플로이드

# n개의 도시에서 모든 도시의 쌍 (A,B)에 대해 최단거리를 구하라.

import sys

inf=sys.maxsize

n=int(sys.stdin.readline())
m=int(sys.stdin.readline())
dp=[[inf]*(n) for _ in range(n)] # 인접행렬 생성

def floyd(): # O(V^3)의 시간복잡도.
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if dp[i][j] > dp[i][k]+dp[k][j]:
                    dp[i][j] = dp[i][k]+dp[k][j]

for _ in range(m):
    a,b,c=map(int,sys.stdin.readline().split())
    if dp[a-1][b-1]>c: # 입력 중 같은 경로의 비용이 여러번 나올 수 있다.
        dp[a-1][b-1]=c

for i in range(n):
    dp[i][i]=0

floyd()

for i in dp:
    for j in i:
        if j == inf:
            print(0,end=' ')
        else:
            print(j,end=' ')
    print()