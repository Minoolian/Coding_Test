# 팰린드롬 ?

# 자연수 N개를 칠판에 적는다. 그 다음, 질문을 총 M번 한다.
# 두 정수 S와 E(1 ≤ S ≤ E ≤ N)로 나타낼 수 있으며, S번째 수부터 E번째 까지 수가 팰린드롬을 이루는지를 물어본다.

import sys

n=int(sys.stdin.readline())
lis=list(map(int,sys.stdin.readline().split()))
dp=[[0]*(n) for _ in range(n)]

for i in range(n): # 길이가 1인 경우는 모두 팰린드롬
    dp[i][i]=1

for i in range(n-1): # 길이가 2인 경우는 확인 후 팰린드롬
    if lis[i]==lis[i+1]:
        dp[i][i+1]=1

for i in range(2,n): # 길이가 3이상인 경우도 확인 후 팰린드롬
    for j in range(n-i):
        if lis[j]==lis[j+i] and dp[j+1][j+i-1]==1:
            # 이미 이전의 길이들은 팰린드롬인 지 확인했기에 그것을 토대로 검사
            dp[j][j+i]=1

for i,j in [list(map(int,sys.stdin.readline().split())) for _ in range(int(sys.stdin.readline()))]:
    print(dp[i-1][j-1])

