# LCS_2

# LCS 문제는 두 수열이 주어졌을 때, 모두의 부분 수열이 되는 수열 중 가장 긴 것을 찾는 문제이다.
# 예를 들어, ACAYKP와 CAPCAK의 LCS는 ACAK가 된다.

S1 = input(); S2 = input()
dp = [["" for _ in range(len(S1) + 1)] for _ in range(len(S2)+1)]

for i in range(1, len(S2)+1):
    for j in range(1, len(S1)+1):
        if S1[j-1]==S2[i-1]: # 최근 두 문자가 같다면
            dp[i][j]=dp[i-1][j-1]+S2[i-1] # 두 문자가 만나기 바로직전(i-1, j-1) 값에 해당 값을 추가(추적)
        else: # 두 문자가 같지 않다면
            if len(dp[i-1][j]) > len(dp[i][j-1]): # 바로 직전의 LCS 중 최대값
                dp[i][j] = dp[i-1][j]
            else:
                dp[i][j] = dp[i][j-1]

print(len(dp[-1][-1]))
print(dp[-1][-1])
