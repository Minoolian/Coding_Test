# 섬 연결하기

# 크루스칼 알고리즘을 이용한 풀이
# https://programmers.co.kr/learn/courses/30/lessons/42861#

def union(x,y):
    x=find(x)
    y=find(y)

    if x!=y:
        parent[y]=x

def find(x):
    if parent[x]==x:
        return x

    return find(parent[x])

def solution(n, costs):
    answer,e=0,0
    costs.sort(key=lambda x:x[2])
    global parent
    parent=[i for i in range(n)]


    for u,v,w in costs:
        if find(u)!=find(v):
            union(u,v)
            answer+=w
            e+=1

        if e==n-1:
            break

    return answer

solution(4,[[0,1,1],[0,2,2],[1,2,5],[1,3,1],[2,3,8]])