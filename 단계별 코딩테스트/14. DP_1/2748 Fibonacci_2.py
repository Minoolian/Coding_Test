import sys

n=int(sys.stdin.readline())
memo=[0 for _ in range(n+1)]
memo[1]=1

for i in range(2,n+1):
    memo[i]=memo[i-1]+memo[i-2]

print(memo[-1]) #-1 인덱스는 마지막을 가리키는 것 같다.

# https://namu.wiki/w/%EB%8F%99%EC%A0%81%20%EA%B3%84%ED%9A%8D%EB%B2%95
# import sys
#
# n=int(sys.stdin.readline())
#
# memo=[0 for _ in range(n+1)]
# def fibo(n):
#     if n<=1:
#         return n
#     if memo[n]!=0:
#         return memo[n]
#     memo[n]=fibo(n-1)+fibo(n-2)
#     return memo[n]
#
# print(fibo(n))


# 단순히 재귀함수를 이용한 피보나치 수열은 중복된 호출이 많기에 비효율적이다
# def fibo(n):
#     if n<=2:
#         return 1
#     return fibo(n-1)+fibo(n-2)
#
# print(fibo(5))