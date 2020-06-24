# 랜선 자르기

# 자체적으로 K개의 랜선을 가지고 N개의 랜선을 만들어야 하는데
# N개를 만들 수 있는 랜선의 최대 길이

import sys

k, n= map(int, sys.stdin.readline().split())
lan = [int(sys.stdin.readline()) for _ in range(k)]

start, end=1, max(lan)

while start <= end: # start와 end가 같아지면, 해당 길이가 적절한 지 확인
    mid=(start+end)//2
    amount=0

    for i in lan:
        amount += i//mid

    if amount>=n: # 요구사항보다 많거나 같으면 더 긴길이가 없는지 조사
        start=mid+1
    else: # 반대로 길이를 줄여서 조사
        end=mid-1

print(end)
