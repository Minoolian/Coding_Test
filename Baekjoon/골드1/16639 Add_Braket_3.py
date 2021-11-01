# 괄호 추가하기 3

# DP를 이용한 풀이
# https://www.acmicpc.net/problem/16639

n=int(input())
expression=input()

l=n//2+1
dp=[[[-2**31,2**31] if i!=j else [int(expression[i*2]),int(expression[i*2])] for i in range(l)] for j in range(l)]

for j in range(1,l):
    for i in range(l-j):
        for k in range(i,i+j):
            for pre in dp[i][k]:
                for post in dp[k+1][i+j]:
                    temp=eval(str(pre)+expression[k*2+1]+str(post))
                    dp[i][i+j][0]=max(dp[i][i+j][0],temp)
                    dp[i][i+j][1]=min(dp[i][i+j][1],temp)

            # temp=eval(''.join(expression[j:i+1]))
            # dp[i//2]=max(dp[i//2],eval(str(dp[(j-2)//2])+expression[j-1]+str(temp)))

print(dp[0][-1][0])
# 실패 (테케는 모두 통과)
# n=int(input())
# expression=input()
#
# dp=[-float('inf') for _ in range(len(expression)//2+1)]
# dp[0]=int(expression[0])
# for i in range(2,len(expression),2):
#     for j in range(i,1,-2):
#         temp=eval(''.join(expression[j:i+1]))
#         dp[i//2]=max(dp[i//2],eval(str(dp[(j-2)//2])+expression[j-1]+str(temp)))
#
# print(dp[-1])
