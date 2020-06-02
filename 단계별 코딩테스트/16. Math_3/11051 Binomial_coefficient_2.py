# 이항계수 2

# N,K 가 주어졌을때 nCk % 10007 를 구하여라

from math import factorial
import sys

n,k=map(int,input().split())
result=factorial(n)//(factorial(k)*factorial(n-k))
print(result%10007)
# nCk = n! / k!(n-k)!