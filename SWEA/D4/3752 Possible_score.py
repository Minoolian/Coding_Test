# 가능한 시험 점수

# DP를 이용한 풀이.
# https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AWHPkqBqAEsDFAUn&categoryId=AWHPkqBqAEsDFAUn&categoryType=CODE

t=int(input())

for tc in range(1, t+1):
    n=int(input())
    score=list(map(int,input().split()))
    dp=[0 for i in range(10001)]
    dp[0]=1

    for i in range(n):
        for j in range(10000, -1, -1):
            if dp[j]:
                dp[j+score[i]]+=1

    result=0
    for i in dp:
        if i:
            result+=1

    print("#{} {}".format(tc, result))