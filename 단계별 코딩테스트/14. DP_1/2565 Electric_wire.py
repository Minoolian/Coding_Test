# 전깃줄

# 두 전봇대 A와 B 사이에 하나 둘씩 전깃줄을 추가하다 보니 전깃줄이 서로 교차하는 경우가 발생하였다. 합선의 위험이 있어 이들 중 몇 개의 전깃줄을 없애 전깃줄이 교차하지 않도록 만들려고 한다.
# 전깃줄이 서로 교차하지 않게 하기 위해 없애야 하는 전깃줄의 최소 개수

import sys

n=int(sys.stdin.readline())
wire=[]
dp=[1 for _ in range(n)]

for _ in range(n):
    wire.append(list(map(int,sys.stdin.readline().split())))

wire.sort(key=lambda x:x[0]) # A 전봇대를 오름차순 정렬
for i in range(n): # LIS를 이루면 전깃줄이 겹치지 않는다.
    for j in range(i):
        if wire[i][1] > wire[j][1]:
            dp[i]=max(dp[i],dp[j]+1)

print(n-max(dp)) # 전체 전깃줄에서 LIS를 이루는 전깃줄을 빼면 겹치는 전깃줄

