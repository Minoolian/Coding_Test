# 상근이의 여행

# N개국을 여행하기로 한다.
# 방학 동안의 비행 스케줄이 주어졌을 때, 상근이가 가장 적은 종류의 비행기를 타고 모든 국가들을 여행할 수 있도록 하자.
# 한 국가에서 다른 국가로 이동할 때 다른 국가를 거쳐가도 된다.

import sys

input=sys.stdin.readline

t=int(input())

for _ in range(t):
    n,m=map(int,input().split())
    for _ in range(m):
        a,b=map(int,input().split())
    print(n-1) #트리를 구성하는 최소 간선의 수 n-1