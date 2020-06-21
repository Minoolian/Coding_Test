# 행렬 곱셈

# (N X M) * (M X K) = (N X K)

n,m = map(int,input().split())
A=[list(map(int,input().split())) for _ in range(n)]

m,k = map(int,input().split())
B=[list(map(int,input().split())) for _ in range(m)]

result=[[0 for _ in range(k)] for _ in range(n)]

for N in range(n):
    for K in range(k):
        for M in range(m):
            result[N][K] += A[N][M]*B[M][K]



