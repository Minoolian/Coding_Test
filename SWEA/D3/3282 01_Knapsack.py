# 0/1 Knapsack

# DP를 이용한 풀이
# https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=3&problemLevel=4&problemLevel=5&contestProbId=AWBJAVpqrzQDFAWr&categoryId=AWBJAVpqrzQDFAWr&categoryType=CODE&problemTitle=&orderBy=RECOMMEND_COUNT&selectCodeLang=PYTHON&select-1=5&pageSize=30&pageIndex=2

t=int(input())
for tc in range(1, t+1):
    n,k=map(int,input().split())
    thing=[list(map(int,input().split())) for _ in range(n)]

    dp=[[0 for _ in range(k+1)] for _ in range(n+1)]
    for i in range(1,n+1):
        for j in range(k+1):
            if thing[i-1][0]>j:
                dp[i][j]=dp[i-1][j]
            else:
                dp[i][j]=max(dp[i-1][j], thing[i-1][1]+dp[i-1][j-thing[i-1][0]])

    print(f"#{tc} {max(dp[n])}")