# 나무 자르기

# 높이가 H보다 큰 나무는 H 위의 부분이 잘릴 것이고, 낮은 나무는 잘리지 않을 것이다.
# 이때, 적어도 M미터의 나무를 집에 가져가기 위해서 절단기에 설정할 수 있는 높이의 최댓값

import sys

n,m = map(int,sys.stdin.readline().split())
lis=list(map(int,sys.stdin.readline().split()))

start, end=1, max(lis)

while start <= end: # start와 end가 같아지면, 해당 길이가 적절한 지 확인
    mid=(start+end)//2
    amount=0

    for i in lis:
        if i>mid:
            amount += i-mid

    if amount>=m: # 요구사항보다 많거나 같으면 더 높이 절단(나무를 덜 벌목)
        start=mid+1
    else: # 반대로 길이를 줄여서 조사
        end=mid-1

print(end)