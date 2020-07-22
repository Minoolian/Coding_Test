# 외판원 순회

# 1번부터 N번까지 번호가 매겨져 있는 도시
# 어느 한 도시에서 출발해 N개의 도시를 모두 거쳐 다시 원래의 도시로 돌아오는 순회 여행 경로 (단, 한번 갔던 도시는 갈 수 없다.)
# 각 도시간에 이동하는데 드는 비용은 행렬 W[i][j]형태로 주어진다. 비용은 대칭적이지 않다.

import sys

n=int(sys.stdin.readline())
inf=sys.maxsize
w=[list(map(int,sys.stdin.readline().split())) for _ in range(n)]

dp=[[None]*(1<<n) for _ in range(n)]

def tsp(cur,visited):
    if visited==(1<<n)-1: # 모든 도시를 방문했다면
        return w[cur][0] or inf # 현재 자리에서 0으로 가는 방법이 없으면 inf 반환

    if dp[cur][visited] != None: # 이미 현재까지의 비용이 계산되어있다면
        return dp[cur][visited] # 그 값을 반환

    tmp=inf
    for city in range(n): # 모든 도시에 대해서
        if visited & (1<<city) ==0 and w[cur][city] !=0: # 그 도시를 방문하지 않았고, 가는 방법도 있다면
            tmp=min(tmp, tsp(city,visited | (1<<city)) + w[cur][city])
            # 그 도시까지의 비용 + 그 도시에서 현재까지의 비용
    dp[cur][visited]=tmp
    return tmp

print(tsp(0,1<<0))

