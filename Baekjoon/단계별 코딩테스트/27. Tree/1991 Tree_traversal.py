# 트리 순회

# 전위 순회: (루트) (왼쪽 자식) (오른쪽 자식)
# 중위 순회: (왼쪽 자식) (루트) (오른쪽 자식)
# 후위 순회: (왼쪽 자식) (오른쪽 자식) (루트)

# 문자 그대로를 인덱스로 사용하기 위해 아스키코드를 이용한 방법도 존재한다.

import sys
sys.setrecursionlimit(10**6)

def pre(node): #전위 순회
    if node=='.':
        return
    print(node, end="")
    pre(tree[node][0])
    pre(tree[node][1])

def inorder(node): #중위 순회
    if node=='.':
        return
    inorder(tree[node][0])
    print(node, end="")
    inorder(tree[node][1])

def post(node): #후위 순회
    if node==".":
        return
    post(tree[node][0])
    post(tree[node][1])
    print(node, end="")

n=int(sys.stdin.readline())
tree={} #딕셔너리를 이용하여 호출

for _ in range(n):
    root, left, right=sys.stdin.readline().split()
    tree[root]=[left,right] #딕셔너리에 값을 저장

pre('A')
print()
inorder('A')
print()
post('A')