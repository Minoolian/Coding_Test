# Contact

# BFS를 이용한 풀이
# https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=3&problemLevel=4&problemLevel=5&contestProbId=AV15B1cKAKwCFAYD&categoryId=AV15B1cKAKwCFAYD&categoryType=CODE&problemTitle=&orderBy=RECOMMEND_COUNT&selectCodeLang=PYTHON&select-1=5&pageSize=30&pageIndex=2

from collections import deque

def bfs(s):
    q=deque()
    q.append([0,s])
    visit[s]=False
    result=[0,0]


    while q:
        level,u=q.popleft()

        if result[0]==level:
            result[1]=max(result[1],u)
        elif result[0]<level:
            result=[level,u]

        for v in m[u]:
            if visit[v]:
                q.append([level+1,v])
                visit[v]=False

    return result[1]

if __name__=="__main__":

    for tc in range(1,11):
        n,s=map(int,input().split())
        lis=list(map(int,input().split()))
        m=[set() for _ in range(n+1)]
        visit=[True for _ in range(n+1)]

        for i in range(0, n, 2):
            m[lis[i]].add(lis[i+1])

        print(f"#{tc} {bfs(s)}")