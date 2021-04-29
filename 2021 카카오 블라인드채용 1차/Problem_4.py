def floyd(dp,n):
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if dp[i][j] > dp[i][k]+dp[k][j]:
                    dp[i][j]=dp[i][k]+dp[k][j]

def find_path(n,s,a,b,dp):
    result=float('inf')
    for k in range(n):
        result=min(result,dp[s-1][k]+dp[k][a-1]+dp[k][b-1])

    return result

def solution(n, s, a, b, fares):

    dp=[[float('inf') if i!=j else 0 for i in range(n)] for j in range(n)]

    for x,y,d in fares:
        dp[x-1][y-1]=d
        dp[y-1][x-1]=d

    floyd(dp,n)

    return find_path(n,s,a,b,dp)




# 플로이드 워셜
# D[i][j] = i ~ j 까지 최단거리
# D[i][j], D[i][k]+D[k][j]