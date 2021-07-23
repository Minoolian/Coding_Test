# 정수 삼각형

#
# https://programmers.co.kr/learn/courses/30/lessons/43105
def solution(triangle):
    dp=[[0]*(i+1) for i in range(len(triangle))]
    dp[0][0]=triangle[0][0]

    for i in range(1,len(triangle)):
        for j in range(i+1):
            if j==0:
                dp[i][j]=dp[i-1][0]+triangle[i][j]
            elif j==i:
                dp[i][j]=dp[i-1][j-1]+triangle[i][j]
            else:
                dp[i][j]=max(dp[i-1][j-1]+triangle[i][j],dp[i-1][j]+triangle[i][j])


    return max(dp[len(triangle)-1])

# 한줄코딩 (타인풀이)
# solution=lambda t,l=[]:max(l) if not t else solution(t[1:],[max(x,y)+z for x,y,z in zip([0]+l,l+[0],t[0])])
