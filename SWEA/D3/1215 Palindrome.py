# 회문

#
# https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV14QpAaAAwCFAYi&categoryId=AV14QpAaAAwCFAYi&categoryType=CODE&&&

import sys

n=int(sys.stdin.readline())
temp=[]
for _ in range(8):
    temp.append(input())
result=0

for lis in temp:
    dp=[[0]*(8) for _ in range(8)]

    for i in range(8): # 길이가 1인 경우는 모두 팰린드롬
        dp[i][i]=1
        result+=1

    for i in range(7): # 길이가 2인 경우는 확인 후 팰린드롬
        if lis[i]==lis[i+1]:
            dp[i][i+1]=1
            result+=1

    for i in range(2,n): # 길이가 3이상인 경우도 확인 후 팰린드롬
        for j in range(n-i):
            if lis[j]==lis[j+i] and dp[j+1][j+i-1]==1:
                # 이미 이전의 길이들은 팰린드롬인 지 확인했기에 그것을 토대로 검사
                dp[j][j+i]=1
                result+=1
print(result)