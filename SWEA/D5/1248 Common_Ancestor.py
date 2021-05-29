# 공통조상

# Tree를 이용한 풀이
# https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=3&problemLevel=4&problemLevel=5&contestProbId=AV15PTkqAPYCFAYD&categoryId=AV15PTkqAPYCFAYD&categoryType=CODE&problemTitle=&orderBy=RECOMMEND_COUNT&selectCodeLang=PYTHON&select-1=5&pageSize=30&pageIndex=2

t=int(input())
for tc in range(1,t+1):
    v,e,v1,v2=map(int,input().split())
    temp=list(map(int,input().split()))
    tree=[[0,1] for _ in range(v+1)]
    tree_rev=[[]]*(v+1)

    for i in range(0,e*2-1,2):
        tree[temp[i+1]][0]=temp[i]
        x=temp[i]
        value=tree[temp[i+1]][1]
        while x:
            tree[x][1]+=value
            x=tree[x][0]

    v1_tree=[v1]
    v2_tree=[v2]

    while tree[v1][0]:
        v1_tree.append(tree[v1][0])
        v1=tree[v1][0]

    while tree[v2][0]:
        v2_tree.append(tree[v2][0])
        v2=tree[v2][0]

    idx_v1=len(v1_tree)-1
    idx_v2=len(v2_tree)-1

    while v1_tree[idx_v1]==v2_tree[idx_v2]:
        idx_v1-=1
        idx_v2-=1

    print(f"#{tc} {v1_tree[idx_v1+1]} {tree[v1_tree[idx_v1+1]][1]}")
