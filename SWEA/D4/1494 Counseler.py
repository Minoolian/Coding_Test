# 사랑의 카운슬러

#
# https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV2b_WPaAEIBBASw&categoryId=AV2b_WPaAEIBBASw&categoryType=CODE

from itertools import permutations

def v(a, b):
    return (a*a) + (b*b)

n=int(input())
worm=[list(map(int,input().split())) for _ in range(n)]

