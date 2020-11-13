# 피보나치 수 3

# [1 1] = [ F2 F1 ] 라고 생각하고 거듭제곱으로 피보나치 수열 풀이.
# [1 0]   [ F1 F0 ]

# [[1,1],[1,0]] 의 거듭제곱 및 행렬곱 이용 (10830과 유사)

n=2

def mul(A,B):
    if B==1:
        for i in range(n):
            for j in range(n):
                A[i][j]%=1000000
        return A

    elif B%2==0:
        result = [[0 for _ in range(n)] for _ in range(n)]
        C=mul(A,B//2)
        for N in range(n):
            for K in range(n):
                for M in range(n):
                    result[N][K] += C[N][M] * C[M][K]
                result[N][K]%=1000000
        return result

    else:
        result = [[0 for _ in range(n)] for _ in range(n)]
        C=mul(A,B-1)
        for N in range(n):
            for K in range(n):
                for M in range(n):
                    result[N][K] += A[N][M] * C[M][K]
                result[N][K]%=1000000
        return result

a=int(input())
A=[[1,1],[1,0]]

if a==0:
    print(0)
elif a==1 or a==2:
    print(1)
else:
    print(sum(mul(A,a-2)[0])%1000000)
