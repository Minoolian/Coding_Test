# 친구 네트워크

# 첫째 줄에 테스트 케이스의 개수
# 각 테스트 케이스의 첫째 줄에는 친구 관계의 수 F
# 다음 F개의 줄에는 친구 관계가 생긴 순서대로 주어진다
# 친구 관계는 두 사용자의 아이디로 이루어져 있으며, 알파벳 대문자 또는 소문자로만 이루어진 길이 20 이하의 문자열

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
        cnt[x]+=cnt[y]

t=int(input())

while t:
    t-=1

    f=int(input())
    lis=[list(input().split()) for _ in range(f)]
    cnt={}
    parent={}
    for a,b in lis:
        if a not in parent:
            parent[a]=a
            cnt[a]=1

        if b not in parent:
            parent[b]=b
            cnt[b]=1

        union(a,b)
        print(cnt[find(a)])



