n, m=map(int,input().split())
check=[False]*(n+1) #유망한 노드인지 확인
result=[0]*m

def dfs(index):

    if index==m: # DFS의 깊이(횟수)가 같으면 결과를 리턴
        for i in range(m):
            print(result[i], end=" ")
        print()
        return

    for i in range(1,n+1):
        if check[i]: # 유망한 노드가 아니면 (True가 유망하지 않은 노드)
            continue
        check[i]=True
        result[index]=i # 결과는 DFS가 진행할 때 덮어씌여 지기 때문에 상관 X
        dfs(index+1)
        check[i]=False # 같은 층의 노드들이 DFS를 진행할 때 영향을 주지 않도록

dfs(0)