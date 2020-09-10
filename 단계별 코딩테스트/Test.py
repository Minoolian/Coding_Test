def rotate(lis):
    n=len(lis[0])
    new=[[None]*n for _ in range(n)]

    for i in range(n):
        for j in range(n):
            new[j][n-1-i]=lis[i][j]

    return new


key=[[0, 0, 0], [1, 0, 0], [0, 1, 1]]
lock=[[1, 1, 1], [1, 1, 0], [1, 0, 1]]

print(rotate(lock))