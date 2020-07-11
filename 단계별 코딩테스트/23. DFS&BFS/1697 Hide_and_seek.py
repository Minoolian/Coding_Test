# 숨바꼭질

# 위치가 X일 때 걷는다면 1초 후에 X-1 또는 X+1로 이동하게 된다. 순간이동을 하는 경우에는 1초 후에 2*X의 위치로 이동
# N이 K를 찾을 수 있는 가장 빠른 시간이 몇 초 후인지 구하는 프로그램

import sys
from collections import deque

def bfs(visit,n,k):
    q=deque([n])

    while q:
        x=q.popleft()

        if k==x:
            return visit[x]

        for i in (x+1, x-1, 2*x): # n이 이동하는 경우
            if visit[i]==0 and (0 <= i < 100001):
                q.append(i)
                visit[i]= visit[x]+1 # 전의 시간에 1을 더한다.


n,k=map(int,sys.stdin.readline().split())
visit=[0]*1000001

print(bfs(visit,n,k))