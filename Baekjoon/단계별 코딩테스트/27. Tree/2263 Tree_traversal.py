# 트리의 순회

# 첫째 줄에 n이 주어진다. 다음 줄에는 인오더를 나타내는 n개의 자연수가 주어지고, 그 다음 줄에는 포스트오더가 주어진다.
# 프리오더를 출력

import sys
sys.setrecursionlimit(10**6)

def preorder(start_in, end_in, start_post, end_post):

    if start_in>end_in or start_post>end_post:
        return

    root=postorder[end_post]
    idx=find[root]

    num=idx-start_in

    print(root, end=" ")
    preorder(start_in, idx-1, start_post, start_post+num-1)
    preorder(idx+1, end_in, start_post+num, end_post-1)


n=int(sys.stdin.readline())
inorder=list(map(int,sys.stdin.readline().split()))
postorder=list(map(int,sys.stdin.readline().split()))
find=[0 for _ in range(n+1)] # 매번 .index() 로 검색하는 것은 비효율적.
for i in range(n): # 전위 순회의 값을 검색하면 인덱스를 반환하는 리스트 작성.
    find[inorder[i]]=i

preorder(0,n-1,0,n-1)