# 카드 2

# 1번 카드가 제일 위에, N번 카드가 제일 아래인 상태로 순서대로 카드가 놓여 있다.
# 제일 위에 있는 카드를 바닥에 버린다. 그 다음, 제일 위에 있는 카드를 제일 아래에 있는 카드 밑으로 옮긴다.
# 제일 마지막에 남게 되는 카드

from collections import deque

n=int(input())
lis=deque([i for i in range(1,n+1)])

while len(lis) !=1:
    lis.popleft() # tail을 pop
    lis.rotate(-1) # 양수면 n만큼 right rotation, 음수면 left rotation

print(lis[-1])



# push() 로 인한 시간복잡도 O(n)
# lis=[i for i in range(int(input()),0,-1)]
#
# while len(lis)>1:
#     lis.pop()
#     lis.insert(0,lis.pop())
#
# print(lis[-1])