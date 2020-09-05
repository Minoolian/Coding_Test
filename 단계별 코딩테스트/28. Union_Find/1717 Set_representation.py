# 집합의 표현

# 첫째 줄에 n, m이 주어진다.
# 다음 m개의 줄에는 각각의 연산이 주어진다
# 합집합은 0 a b의 형태 / 같은 집합에 포함되어 있는지를 확인하는 연산은 1 a b의 형태
#
# 1로 시작하는 입력에 대해서 한 줄에 하나씩 YES/NO로 결과

# Union Find를 이용한 풀이
import sys
input=sys.stdin.readline

def find(x):
    if parent[x]==x:
        return x
    parent[x]=find(parent[x])
    return parent[x]

def union(x,y):
    x=find(x)
    y=find(y)

    if x!=y:
        parent[y]=x

def find_parent(x):
    if parent[x]==x:
        return x
    return find_parent(parent[x])

n,m=map(int,input().split())
parent={}

for i in range(n+1):
    parent[i]=i

for _ in range(m):
    cmd,num_1,num_2=map(int,input().split())

    if not cmd:
        union(num_1,num_2)

    if cmd:
        if find_parent(num_1)==find_parent(num_2):
            print('YES')
        else:
            print('NO')
# 메모리 초과
# import sys
#
# n,m=map(int,sys.stdin.readline().split())
#
# a=[]
# for i in range(n+1):
#     a.append(set([i]))
#
# lis=[list(map(int,sys.stdin.readline().split())) for _ in range(m)]
#
# for i in lis:
#     if i[0]==0:
#         a[i[1]]=a[i[1]]|a[i[2]]
#         a[i[2]]=a[i[1]]|a[i[2]]
#     else:
#         if i[1]==i[2]:
#             print("YES")
#         else:
#             print("NO")


