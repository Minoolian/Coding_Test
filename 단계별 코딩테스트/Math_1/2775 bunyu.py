apt = [[0 for col in range(15)] for row in range(15)]

for k in range(15):
    for n in range(1, 15):
        if k == 0:
            apt[k][n] = n
        else:
            apt[k][n] = apt[k][n - 1] + apt[k - 1][n]
T = int(input())

for _ in range(T):
    K = int(input())
    N = int(input())
    print(apt[K][N])