# 가장 가까운 공통 조상

# 테스트 케이스의 개수 T
# 첫째 줄에 트리를 구성하는 노드의 수 N
# 다음 N-1개의 줄에 트리를 구성하는 간선 정보
# 한 간선 당 한 줄에 두 개의 숫자 A B 가 순서대로 주어지는데, 이는 A가 B의 부모라는 뜻
# 테스트 케이스의 마지막 줄에 가장 가까운 공통 조상을 구할 두 노드

import sys
input=sys.stdin.readline

t=int(input())

for _ in range(t):
    n=int(input())
    tree=[0 for _ in range(n+1)]

    for _ in range(n-1):
        p,c=map(int,input().split())
        tree[c]=p # 각 노드의 부모 저장

    a,b=map(int,input().split())
    a_parent=[a]
    b_parent=[b]

    while tree[a]:
        a_parent.append(tree[a]) # a의 부모를 따라 리스트에 입력
        a=tree[a]

    while tree[b]:
        b_parent.append(tree[b]) # b의 부모를 따라 리스트에 입력
        b=tree[b]

    a_rank=len(a_parent)-1
    b_rank=len(b_parent)-1

    while a_parent[a_rank]==b_parent[b_rank]: # root 부터 아래로 훑는다.
        # 다른 값이 나오면 그 전의 값이 가장 가까운 공통조상
        a_rank-=1
        b_rank-=1

    print(a_parent[a_rank+1])
