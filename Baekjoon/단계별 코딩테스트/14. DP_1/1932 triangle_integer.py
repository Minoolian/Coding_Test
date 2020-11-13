import sys

n=int(sys.stdin.readline())
tri=[list(map(int,sys.stdin.readline().split())) for _ in range(n)]

# 2차원 배열로 트리 구조를 표현
for i in range(n-1): # 층을 나타내는 i
    for j in range(len(tri[i+1])): # 각 층의 원소를 나타내는 j
        if j==0: # 제일 앞의 원소는 전 층의 하나의 값만 고려한다.
            tri[i+1][j]+=tri[i][j]
        elif i+1==j: # 제일 끝의 원소는 전 층의 하나의 값만 고려한다
            tri[i+1][j]+=tri[i][j-1]
        else: # 가운데 원소들은 전 층의 두 원소 중 큰 것을 더한다.
            tri[i+1][j]+=max(tri[i][j-1],tri[i][j])

print(max(tri[n-1])) # max(tri[-1])