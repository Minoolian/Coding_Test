# N으로 표현

# DP를 이용한 풀이
# https://programmers.co.kr/learn/courses/30/lessons/42895

def solution(N, number):
    dp=[set() for _ in range(9)]
    dp[1].add(N)

    if N==number:
        return 1

    for i in range(2,9):
        dp[i].add(int(str(N)*i))
        for j in range(1,i//2+1):
            for n in dp[j]:
                for m in dp[i-j]:
                    dp[i].add(n+m)
                    dp[i].add(n-m)
                    dp[i].add(m-n)
                    dp[i].add(n*m)
                    if m!=0: dp[i].add(n//m)
                    if n!=0: dp[i].add(m//n)
        if number in dp[i]:
            return i

    return -1

print(solution(5,31168))
