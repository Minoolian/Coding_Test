# 이항계수 1

# N,K 가 주어졌을때 nCk 를 구하여라

from math import factorial

n,k=map(int,input().split())
print(factorial(n)//(factorial(k)*factorial(n-k)))
# nCk = n! / k!(n-k)!