from copy import deepcopy # 다차원 리스트의 복사는 깊은 복사로 해야한다.

def rotate(lis):
    n=len(lis[0])
    new=[[None]*n for _ in range(n)]

    for i in range(n):
        for j in range(n):
            new[j][n-1-i]=lis[i][j]

    return new

def check(lis,m,n):

    for i in range(m,m+n):
        for j in range(m,m+n):
            if lis[i][j]!=1:
                return False
    return True


def solution(key, lock):
    n=len(lock[0])
    m=len(key[0])
    new_lock=[[0]*(n+2*m) for _ in range(n+2*m)]

    for i in range(m,m+n):
        for j in range(m,m+n):
            new_lock[i][j]=lock[i-m][j-m]

    for _ in range(4):
        for i in range(m+n+1):
            for j in range(m+n+1):
                check_lock=deepcopy(new_lock)
                for a in range(m):
                    for b in range(m):
                        check_lock[i+a][j+b]+=key[a][b]
                if check(check_lock,m,n):
                    return True
        if m!=1:
            new_lock=rotate(new_lock)
        else:
            return False
    return False


if __name__ == "__main__":
    key=[[0, 0, 0], [1, 0, 0], [0, 1, 1]]
    lock=[[1, 1, 1], [1, 1, 0], [1, 0, 1]]

    print(solution(key,lock))