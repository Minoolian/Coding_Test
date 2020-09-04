# 집합의 표현

# 첫째 줄에 n, m이 주어진다.
# 다음 m개의 줄에는 각각의 연산이 주어진다
# 합집합은 0 a b의 형태 / 같은 집합에 포함되어 있는지를 확인하는 연산은 1 a b의 형태
#
# 1로 시작하는 입력에 대해서 한 줄에 하나씩 YES/NO로 결과

import sys

n,m=map(int,sys.stdin.readline().split())

a=[]
for i in range(n+1):
    a.append(set([i]))

lis=[list(map(int,sys.stdin.readline().split())) for _ in range(m)]

for i in lis:
    if i[0]==0:
        a[i[1]]=a[i[1]]|a[i[2]]
        a[i[2]]=a[i[1]]|a[i[2]]
    else:
        if i[1]==i[2]:
            print("YES")
        else:
            print("NO")


