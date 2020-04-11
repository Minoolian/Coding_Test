T = int(input())

for _ in range(T):
    x, y = map(int, input().split())
    gap=y-x
    a = 1
    while True:
        if gap <= a ** 2:
            if gap > a ** 2 - a:
                print(2 * a - 1)
                break
            else:
                print(2 * a - 2)
                break
        a+=1

# 워프 거리가 완전 대칭이 되는 구간을 기준으로 하였다. (제곱수가 기준)
# n-1개(2n-2 번 워프), n개(2n-1 번 워프) <= n^2 기준