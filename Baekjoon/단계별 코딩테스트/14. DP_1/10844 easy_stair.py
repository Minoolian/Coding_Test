# n번째 k로 시작하는 계단 수는 n-1번째의 k-1, k+1번째로 시작하는 계단수의 합

import sys

dp = [[0 for _ in range(100)] for _ in range(10)]

for j in range(100):
    for i in range(10):
        if j == 0:
            dp[i][j] = 1
        else:
            if i == 0:
                dp[i][j] = dp[i + 1][j - 1]
            elif i == 9:
                dp[i][j] = dp[i - 1][j - 1]
            else:
                dp[i][j] = dp[i - 1][j - 1] + dp[i + 1][j - 1]

n = int(sys.stdin.readline())
print(sum([i[n-1] for i in dp[1:10]]) % 1000000000) # 1행~9행의 0번째 원소들의 리스트 합
# dp 리스트 자체의 행,열을 뒤집어 해결하면 dp[n-1][1:10] 으로 해결 가능

# dp[1:10][2] 앞에서 먼저 슬라이싱이 이루어지면 1~9 행 중 2번째 행의 의미가 된다.
# test=[[1,2,3],[4,5,6],[7,8,9]]
#
# print(test[:3][1])
#
# 결과 : [4,5,6]
