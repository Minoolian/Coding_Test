# 해당 방법은 브루트포스 방법에 근접하고, itertools 모듈의 순열을 생성해주는 permutation 메서드를 사용해서 구성할 수도 있다.
import sys

n = int(sys.stdin.readline())
num = list(map(int, sys.stdin.readline().split()))
operater = list(map(int, sys.stdin.readline().split()))

max_num = -100000000; min_num = 1000000000


def dfs(result, index, a, b, c, d):
    global num, max_num, min_num

    if index == n - 1:
        max_num = max(result, max_num)
        min_num = min(result, min_num)
        return

    else:
        if a:
            dfs(result + num[index + 1], index + 1, a - 1, b, c, d)
        if b:
            dfs(result - num[index + 1], index + 1, a, b - 1, c, d)
        if c:
            dfs(result * num[index + 1], index + 1, a, b, c - 1, d)
        if d:
            if result < 0:
                dfs(-(abs(result) // num[index + 1]), index + 1, a, b, c, d - 1)
            else:
                dfs(result // num[index + 1], index + 1, a, b, c, d - 1)


dfs(num[0], 0, operater[0], operater[1], operater[2], operater[3])
print(max_num)#, min_num, sep='\n')
print(min_num)
