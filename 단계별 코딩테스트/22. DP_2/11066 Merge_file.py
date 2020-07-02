# 파일 합치기

# 두 개의 파일을 합쳐서 하나의 임시파일을 만들고,
# 이 임시파일이나 원래의 파일을 계속 두 개씩 합쳐서 소설의 여러 장들이 연속이 되도록 파일을 합쳐나가고,
# 최종적으로는 하나의 파일로 합친다.
# 필요한 비용(시간 등)이 두 파일 크기의 합이라고 가정할 때, 필요한 최소비용을 계산.

# knuth's optimization 을 이용해서 수행시간을 최소화하는 방법도 존재한다.

import sys

t=int(sys.stdin.readline())
for _ in range(t):
    n=int(sys.stdin.readline())
    lis=list(map(int,sys.stdin.readline().split()))

    dp=[[0 for _ in range(n+1)] for _ in range(n+1)] # NXN memoization
    # dp[i][j]: i번째부터 j번째까지의 합친 파일크기의 최소
    sum=[0]*(n+1)

    for i in range(1,n+1):
        # 각 파일의 크기들의 누적합을 저장 (가중치를 계속 더해주어야 하므로 사용)
        # ex) 2번째 파일 ~ 5번째 파일의 합 = 5번째 파일까지의 합 - 1번째 파일까지의 합
        sum[i]=sum[i-1]+lis[i-1]

    for x in range(1,n+1): # 최종 결과를 얻기 위해서는 우측 아래로 대각선으로 먼저 채워나가야 한다. (x는 자리 잡기위한 용도)
        for i in range(n-x): # 대각선은 점점 줄어듦으로 x만큼 줄인다.
            j=i+x # 대각선 원소의 i와 j는 고정된 x만큼의 차이가 난다.
            dp[i][j]=sys.maxsize
            for k in range(i,j):
                dp[i][j]=min(dp[i][j],dp[i][k]+dp[k+1][j]+sum[j+1]-sum[i])

    print(dp[0][n-1])