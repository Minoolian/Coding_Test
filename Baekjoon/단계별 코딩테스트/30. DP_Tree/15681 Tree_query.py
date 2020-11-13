# 트리와 쿼리

# 간선에 가중치와 방향성이 없는 임의의 루트 있는 트리가 주어졌을 때
# 정점 U를 루트로 하는 서브트리에 속한 정점의 수를 출력
#
# 트리의 정점의 수 N과 루트의 번호 R, 쿼리의 수 Q가 주어진다.
# 이어 N-1줄에 걸쳐, U V의 형태로 트리에 속한 간선의 정보가 주어진다.
# 이는 U와 V를 양 끝점으로 하는 간선이 트리에 속함을 의미한다.
# 이어 Q줄에 걸쳐, 문제에 설명한 U가 하나씩 주어진다.

import sys
sys.setrecursionlimit(10**6)
input=sys.stdin.readline

def count(r):
    node_count[r]=1
    for node in tree[r]:
        if not node_count[node]:
            count(node)
            node_count[r]+=node_count[node]
    return

if __name__=="__main__":
    n,r,q=map(int,input().split())
    tree=[[] for _ in range(n+1)]
    node_count=[0]*(n+1)

    for _ in range(n-1):
        u,v=map(int,input().split())
        tree[u].append(v)
        tree[v].append(u)

    count(r)

    for _ in range(q):
        q=int(input())
        print(node_count[q])