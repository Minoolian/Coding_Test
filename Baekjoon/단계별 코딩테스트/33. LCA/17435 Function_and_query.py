# 합성함수와 쿼리

# f4(1) = f(f(f(f(1))))이다.

# 첫 줄에 정수 m이 주어진다.
# 다음 줄에 f(1), f(2), ..., f(m)이 차례대로 주어진다.
# 다음 줄에 쿼리의 개수 Q가 주어진다.
# 다음 Q개의 줄에 각각 정수 n과 x가 주어진다.
#
# 주어지는 n, x마다 fn(x)를 출력한다.

import sys
input=sys.stdin.readline

m=int(input())
f=[0]+list(map(int,input().split()))
dp=[[f[i]] for i in range(m+1)]
# dp[i][j]: 정점 i에서 2^j 만큼 이동했을 때의 정점
# 마치 분할정복의 A^B 연산할 때 연산횟수를 줄이는 것과 유사

for j in range(1,19):
    for i in range(1,m+1):
        dp[i].append(dp[dp[i][j-1]][j-1])
        # i에서 2^j번 이동 후 정점은 i에서 2^(j-1)*2번 이동하는 것과 같다.
        # Sparse(희소) table 구성
        # 모든 값을 구성하는 것이 아닌 일부로 구성

q=int(input())
for _ in range(q):
    n,x=map(int,input().split())
    for j in range(18, -1, -1):
        if n>= 1<<j: # 2^j 보다 입력받은 fn(x)의 n이 더 크다면
            n-= 1<<j # 2^j를 빼고 나머지를 계산
            x=dp[x][j] # 끝까지 탐색하는 양상

    print(x)