# 괄호 추가하기 3

#
# https://www.acmicpc.net/problem/16639

n=int(input())
expression=input()

l=n//2+1
dp=[[[-float('inf'),float('inf')] if i!=j else [int(expression[i*2]),int(expression[i*2])] for i in range(l)] for j in range(l)]

for j in range(1,l):
    for i in range(l-i):
        for k in range(i+1,)
        temp=eval(''.join(expression[j:i+1]))
        dp[i//2]=max(dp[i//2],eval(str(dp[(j-2)//2])+expression[j-1]+str(temp)))

print(dp[-1])

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
