# 경찰차

# 도로의 개수를 나타내는 정수 N, 처리해야 하는 사건의 개수를 나타내는 정수 W, 사건이 발생된 위치가 한 줄에 하나씩 주어진다.
# 두 경찰차가 이동한 총 거리, 사건이 맡겨진 경찰차 번호 1 또는 2를 출력

# 전형적인 DP로 구현
import sys
from collections import deque

def dist(a,b):
    if a==[0,0]:
        return abs(1-b[0])+abs(1-b[1])
    elif b==[0,0]:
        return abs(a[0]-n)+abs(a[1]-n)
    else:
        return abs(a[0]-b[0])+abs(a[1]-b[1])

n=int(sys.stdin.readline())
w=int(sys.stdin.readline())
lis=[[0,0]]+[list(map(int,sys.stdin.readline().split())) for _ in range(w)]

inf=sys.maxsize
dp=[[inf]*(w+1) for _ in range(w+1)]

for i in range(1,w+1): # 1. 한 경찰차만 모든 사건에 출동할 경우
    if i==1:
        dp[i][0]=dist(lis[i-1],lis[i])
        dp[0][i]=dist(lis[i],lis[i-1])
    else:
        dp[i][0]=dp[i-1][0]+dist(lis[i-1],lis[i])
        dp[0][i]=dp[0][i-1]+dist(lis[i],lis[i-1])


for i in range(1,w): # 2. 1을 제외한 모든 경우의 수
    for j in range(i+1,w+1):
        if abs(i-j)!=1: # 1차이가 나지 않을 경우 한가지의 경우만 존재
            dp[j][i] = dp[j-1][i]+dist(lis[j-1],lis[j])
            dp[i][j] = dp[i][j-1]+dist(lis[j],lis[j-1])
        else: # 1차이가 날 경우 여러가지 경우를 고려
            for k in range(0,j-1): #
                dp[j][i] = min(dp[j][i], dp[k][i]+dist(lis[k],lis[j]))
                dp[i][j] = min(dp[i][j], dp[i][k]+dist(lis[j],lis[k]))
mini=inf
for x in range(w+1): # 3. 최솟값을 찾는다.
    if mini>dp[w][x]:
        mini=dp[w][x]
        idx_x=w
        idx_y=x
    if mini>dp[x][w]:
        mini=dp[x][w]
        idx_x=x
        idx_y=w
print(mini)

result=deque()
while True:
    if idx_x==1 and idx_y==0:
        result.appendleft(1)
        break
    elif idx_x==0 and idx_y==1:
        result.appendleft(2)
        break

    if abs(idx_x-idx_y)!=1:
        if idx_x > idx_y:
            result.appendleft(1)
            idx_x=idx_x-1
        else:
            result.appendleft(2)
            idx_y=idx_y-1
    else:
        if idx_x > idx_y:
            for k in range(idx_x-1):
                if dp[idx_x][idx_y]-dist(lis[k],lis[idx_x])==dp[k][idx_y]:
                    idx_x=k
            result.appendleft(1)
        else:
            for k in range(idx_y-1):
                if dp[idx_x][idx_y]-dist(lis[idx_y],lis[k])==dp[idx_x][k]:
                    idx_y=k
            result.appendleft(2)

for i in result:
    print(i)

# Trace 리스트를 추가하여 코드 간결하게 만들기
# import sys
# from collections import deque
#
# def dist(a,b):
#     if a==[0,0]:
#         return abs(1-b[0])+abs(1-b[1])
#     elif b==[0,0]:
#         return abs(a[0]-n)+abs(a[1]-n)
#     else:
#         return abs(a[0]-b[0])+abs(a[1]-b[1])
#
# n=int(sys.stdin.readline())
# w=int(sys.stdin.readline())
# lis=[[0,0]]+[list(map(int,sys.stdin.readline().split())) for _ in range(w)]
#
# print(lis)
#
# inf=sys.maxsize
# dp=[[inf]*(w+1) for _ in range(w+1)]
# trace=[[0]*(w+1) for _ in range(w+1)]
#
# for i in range(1,w+1): # 1. 한 경찰차만 모든 사건에 출동할 경우
#     if i==1:
#         dp[i][0]=dist(lis[i-1],lis[i])
#         trace[i][0]=i-1 ##
#         dp[0][i]=dist(lis[i],lis[i-1])
#         trace[0][i]=i-1 ##
#     else:
#         dp[i][0]=dp[i-1][0]+dist(lis[i-1],lis[i])
#         trace[i][0]=i-1 ##
#         dp[0][i]=dp[0][i-1]+dist(lis[i],lis[i-1])
#         trace[0][i]=i-1 ##
#
#
# for i in range(1,w): # 2. 1을 제외한 모든 경우의 수
#     for j in range(i+1,w+1):
#         if abs(i-j)!=1: # 1차이가 나지 않을 경우 한가지의 경우만 존재
#             dp[j][i] = dp[j-1][i]+dist(lis[j-1],lis[j])
#             trace[j][i]=j-1
#             dp[i][j] = dp[i][j-1]+dist(lis[j],lis[j-1])
#             trace[i][j]=j-1
#         else: # 1차이가 날 경우 여러가지 경우를 고려
#             for k in range(0,j-1): #
#                 if dp[j][i]>dp[k][i]+dist(lis[k],lis[j]):
#                     dp[j][i]=dp[k][i]+dist(lis[k],lis[j])
#                     trace[j][i]=k
#                 if dp[i][j]>dp[i][k]+dist(lis[j],lis[k]):
#                     dp[i][j]=dp[i][k]+dist(lis[j],lis[k])
#                     trace[i][j]=k
#
# mini=inf
# for x in range(w+1): # 3. 최솟값을 찾는다.
#     if mini>dp[w][x]:
#         mini=dp[w][x]
#         idx_x=w
#         idx_y=x
#     if mini>dp[x][w]:
#         mini=dp[x][w]
#         idx_x=x
#         idx_y=w
# print(mini)
#
# result=deque()
# while idx_x!=0 or idx_y!=0:
#     if idx_y>idx_x:
#         idx_y=trace[idx_x][idx_y]
#         result.appendleft(2)
#     else:
#         idx_x=trace[idx_x][idx_y]
#         result.appendleft(1)
#
# for i in result:
#     print(i)



# 재귀 함수로 구현: 시간 초과
# import sys
# sys.setrecursionlimit(10 ** 9) # 재귀 함수의 깊이 설정
#
# def dist(a,b): # 거리를 구하는 함수
#     return abs(a[0]-b[0])+abs(a[1]-b[1])
#
# def solve(x,y):
#
#     if x==w or y==w:
#         return 0
#
#     next=max(x,y)+1 # 다음사건의 번호
#
#     if x==0: d1=dist(lis[next],[1,1]) # 1번차가 한번도 출동하지 않았다면.
#     else: d1=dist(lis[next],lis[x])
#
#     if y==0: d2=dist(lis[next],[n,n]) # 2번차가 한번도 출동하지 않았다면
#     else: d2=dist(lis[next],lis[y])
#
#     p1=solve(next,y)+d1
#     p2=solve(x,next)+d2
#
#     res=min(p1,p2) # 재귀호출하며 최소값을 반환
#
#     if res==p1:
#         dp[next][y]=res
#     else:
#         dp[x][next]=res
#
#     return res
#
# def track(x, y, min):
#
#     if x==w or y==w:
#         return;
#
#     next=max(x,y)+1
#
#     if x==0: d1=dist(lis[next],[1,1]) # 1번차가 한번도 출동하지 않았다면.
#     else: d1=dist(lis[next],lis[x])
#
#     if y==0: d2=dist(lis[next],[n,n]) # 2번차가 한번도 출동하지 않았다면
#     else: d2=dist(lis[next],lis[y])
#
#     if dp[next][y]>=min:
#         print(1)
#         min-=d1
#         track(next,y,min)
#     else:
#         print(2)
#         min-=d2
#         track(x,next,min)
#     return;
#
#
# n=int(sys.stdin.readline())
# w=int(sys.stdin.readline())
# lis=[[0]]+[list(map(int,sys.stdin.readline().split())) for _ in range(w)]
#
# dp=[[-1 for _ in range(w+1)] for _ in range(w+1)]
#
# min=solve(0,0)
# print(min)
# track(0,0,min)