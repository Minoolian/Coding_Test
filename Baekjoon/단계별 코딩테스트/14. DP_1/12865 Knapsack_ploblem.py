# 배낭문제(0-1 Knapsack Problem)
# 보통 Fractional(쪼개지는) 배낭문제는 그리디 알고리즘으로 해결한다.

# N개의 물건이 있다. 각 물건은 무게 W와 가치 V를 가지는데, 해당 물건을 배낭에 넣어서 가면 V만큼 즐길 수 있다.
# 최대 K무게까지의 배낭만 들고 다닐 수 있다. 최대한 즐거운 여행을 하기 위해 배낭에 넣을 수 있는 물건들의 가치의 최댓값을 구하라.

n,k=map(int,input().split())
knap=[list(map(int,input().split())) for _ in range(n)]

dp=[[0 for _ in range(k+1)] for _ in range(n+1)]

for i in range(1,n+1):
    for j in range(1,k+1):

        if knap[i-1][0] > j:
            dp[i][j]=dp[i-1][j]
        else:
            dp[i][j]=max(knap[i-1][1]+dp[i-1][j-knap[i-1][0]], dp[i-1][j])

        # Knap[i, W] = Knap[i-1, W]                            { if w_i > W }
        #              max(Knap[i-1, W], Knap[i-1, W-w_i]+v_i) { else }
        # 2D 표를 이용해서 표현해 보도록 하자.

print(dp[-1][-1])
