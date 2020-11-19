# 회문2

# DP를 이용한 풀이.
# https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV14Rq5aABUCFAYi&categoryId=AV14Rq5aABUCFAYi&categoryType=CODE


def reverse(temp):
    lis=[[] for _ in range(100)]
    idx=0

    for i in temp:
        for a in i:
            lis[idx].append(a)
            idx+=1
        idx=0

    return lis


def palindrome(temp):
    result=1

    for lis in temp:
        dp=[[0]*100 for _ in range(100)]


        for i in range(100): # 길이가 1인 경우는 모두 팰린드롬
            dp[i][i]=1

        p=1
        for i in range(99): # 길이가 2인 경우는 확인 후 팰린드롬
            if lis[i]==lis[i+1]:
                dp[i][i+1]=1
                if p<2: p=2

        for i in range(2,100): # 길이가 3이상인 경우도 확인 후 팰린드롬
            for j in range(100-i):
                if lis[j]==lis[j+i] and dp[j+1][j+i-1]==1:
                    # 이미 이전의 길이들은 팰린드롬인 지 확인했기에 그것을 토대로 검사
                    dp[j][j+i]=1
                    if p<i+1: p=i+1

        result=max(result, p)

    return result

if __name__=="__main__":

    for tc in range(1, 11):
        input()
        temp=[input() for _ in range(100)]

        print("#{} {}".format(tc, max(palindrome(temp),palindrome(reverse(temp)))))