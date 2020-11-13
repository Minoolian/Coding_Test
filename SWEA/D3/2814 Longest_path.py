# 최장 경로

# DFS를 이용한 풀이
# https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV7GOPPaAeMDFAXB&categoryId=AV7GOPPaAeMDFAXB&categoryType=CODE&&&

def dfs(start):

    result=0
    visit[start]=False
    for v in g[start]:
        if visit[v]:
            result= max(result, dfs(v))

    visit[start]=True
    if not result:
        return 1
    else:
        return result+1


t=int(input())
for tc in range(1, t+1):
    n, m=map(int,input().split())
    g=[[] for _ in range(n+1)]

    for _ in range(m):
            u, v=map(int,input().split())
            g[u].append(v)
            g[v].append(u)

    max_len=0
    for i in range(1,n+1):
        visit=[True]*(n+1)

        max_len=max(max_len,dfs(i))

    print("#{} {}".format(tc,max_len))