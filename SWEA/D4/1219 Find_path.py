# 길찾기

# DFS를 이용한 풀이
# https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV14geLqABQCFAYD&categoryId=AV14geLqABQCFAYD&categoryType=CODE

def dfs(v):
    if v==99:
        return True
    
    for nv in path[v]:
        if dfs(nv):
            return True
    
    return False


for tc in range(1,11):
    t, m=map(int, input().split())
    path=[[] for _ in range(100)]

    tmp=list(map(int,input().split()))

    for i in range(m):
        path[tmp[2*i]].append(tmp[2*i+1])

    if dfs(0):
        print("#{} {}".format(tc,1))
    else:
        print("#{} {}".format(tc,0))
