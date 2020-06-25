# 공유기 설치

# 집 N개가 수직선 위에 있다. 각각의 집의 좌표는 x1, ..., xN이고, 집 여러개가 같은 좌표를 가지는 일은 없다.
# C개의 공유기를 N개의 집에 적당히 설치해서, 가장 인접한 두 공유기 사이의 거리를 최대로 하는 프로그램

import sys

n,c = map(int,sys.stdin.readline().split())
lis=[int(sys.stdin.readline()) for _ in range(n)]

lis.sort()
start, end=1, lis[-1]-lis[0] # 최소 거리, 최대 거리

while start <= end: # start와 end가 같아지면, 해당 길이가 적절한 지 확인
    mid=(start+end)//2
    count=1

    cur=lis[0]
    for i in range(1,n):
        if lis[i]-cur >= mid: # 간격이 적어도 설정한 mid 보다 크거나 같으면
            count+=1
            cur=lis[i] # 설치 위치 갱신

    if count >=c: # 간격을 늘려서 더 넓게 설치할 수 있는지 확인
        start= mid+1
    else:
        end=mid-1

print(end)