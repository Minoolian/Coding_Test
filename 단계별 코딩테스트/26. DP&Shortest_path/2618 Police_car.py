# 경찰차

# 도로의 개수를 나타내는 정수 N, 처리해야 하는 사건의 개수를 나타내는 정수 W, 사건이 발생된 위치가 한 줄에 하나씩 주어진다.
# 두 경찰차가 이동한 총 거리, 사건이 맡겨진 경찰차 번호 1 또는 2를 출력

import sys

def dist(a,b): # 거리를 구하는 함수
    return abs(a[0]-b[0])+abs(a[1]-b[1])

def solve(x,y):

    if x==w or y==w:
        return 0

    next=max(x,y)+1 # 다음사건의 번호

    if x==0: d1=dist(lis[next],[1,1]) # 1번차가 한번도 출동하지 않았다면.
    else: d1=dist(lis[next],lis[x])

    if y==0: d2=dist(lis[next],[n,n]) # 2번차가 한번도 출동하지 않았다면
    else: d2=dist(lis[next],lis[y])

    p1=solve(next,y)+d1
    p2=solve(x,next)+d2

    res=min(p1,p2) # 재귀호출하며 최소값을 반환
    return res


n=int(sys.stdin.readline())
w=int(sys.stdin.readline())
lis=[[0]]+[list(map(int,sys.stdin.readline().split())) for _ in range(w)]

inf=sys.maxsize
dp=[[inf for _ in range(w+1)] for _ in range(w+1)]

print(solve(0,0))