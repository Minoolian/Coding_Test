# 동전 1

# n가지 종류의 동전이 있다. 각각의 동전이 나타내는 가치는 다르다.
# 이 동전을 적당히 사용해서, 그 가치의 합이 k원이 되도록 하고 싶다. 그 경우의 수

import sys

n,k = map(int,sys.stdin.readline().split())
lis=[int(sys.stdin.readline()) for _ in range(n)]
dp=[0 for _ in range(k+1)]
dp[0]=1

for i in lis: # 각 코인의 가치마다 돌린다.
    for j in range(i, k+1): # 코인의 가치보다 낮은 값은 메모이제이션 할 수 없으므로 배제.
        dp[j]+=dp[j-i]
        # 지금 돌리고있는 코인의 가치 를 뺀 값을 메모이제이션 한다.
        # 코인의 가치를 뺀 값 + 코인의 가치만 더해주면 해당 가치이기 때문에

print(dp[k])