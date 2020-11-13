# 숫자카드 2

# 숫자 카드 N개를 가지고 있다. 정수 M개가 주어졌을 때, 이 수가 적혀있는 숫자 카드를 몇 개 가지고 있는지 구하는 프로그램

from collections import Counter
# 이진탐색 방법보다는 딕셔너리 기반의 key-value 로 찾는 방법이 수월하다.

n=int(input())
a=list(map(int,input().split()))
m=int(input())
b=list(map(int,input().split()))

lis=Counter(a)

for i in b:
    if i in lis:
        print(lis[i], end=" ")
    else:
        print(0, end=" ")