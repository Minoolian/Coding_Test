# 행렬 제곱

# N X N 행렬의 거듭제곱의 결과를 mod 1000 한 결과를 출력.

def mul(A,B): # 앞선 O(logN)의 거듭제곱과 행렬곱의 응용이다.
    if B==1:
        for i in range(n):
            for j in range(n):
                A[i][j]%=1000
        return A

    elif B%2==0:
        result = [[0 for _ in range(n)] for _ in range(n)]
        C=mul(A,B//2)
        for N in range(n):
            for K in range(n):
                for M in range(n):
                    result[N][K] += C[N][M] * C[M][K]
                result[N][K]%=1000
        return result

    else:
        result = [[0 for _ in range(n)] for _ in range(n)]
        C=mul(A,B-1)
        for N in range(n):
            for K in range(n):
                for M in range(n):
                    result[N][K] += A[N][M] * C[M][K]
                result[N][K]%=1000
        return result

n,B=map(int,input().split())
A=[list(map(int,input().split())) for _ in range(n)]


for i in mul(A,B):
    print(" ".join(map(str,i)))