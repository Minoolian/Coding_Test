# 구간 합 구하기 4

# 수 N개가 주어졌을 때, i번째 수부터 j번째 수까지 합을 구하는 프로그램

# 첫째 줄에 수의 개수 N, 합을 구해야 하는 횟수 M이 주어진다.
# 둘째 줄에는 N개의 수가 주어진다.
# 셋째 줄부터 M개의 줄에는 합을 구해야 하는 구간 i와 j가 주어진다.

import sys
from math import log
input=sys.stdin.readline


def init(arr, tree, node, start, end):
    if start==end:
        tree[node]=arr[start]
        return tree[node]

    mid=(start+end)//2

    tree[node]=init(arr, tree, node*2, start, mid)+init(arr, tree, node*2+1, mid+1, end)
    return tree[node]

def update(tree, node, start, end, idx, diff):

	if not (start<=idx and idx<=end):
		return

	tree[node]+=diff

	if(start!=end):
		mid=(start+end)//2
		update(tree, node*2, start, mid, idx, diff)
		update(tree, node*2+1, mid+1, end, idx, diff)

def sum(tree, node, start, end, left, right):

	if left>end or right<start:
		return 0

	elif left<=start and end<=right:
		return tree[node]

	mid=(start+end)//2
	return sum(tree, node*2, start, mid, left, right)+sum(tree, node*2+1, mid+1, end, left, right)


if __name__=="__main__":
    n,m=map(int,input().split())
    arr=list(map(int,input().split()))
    tree=[0 for _ in range(4*n+1)]

    init(arr, tree, 1, 0, n-1)

    for _ in range(m):
        left, right=map(int,input().split())
        print(sum(tree, 1, 0, n-1, left-1, right-1))
