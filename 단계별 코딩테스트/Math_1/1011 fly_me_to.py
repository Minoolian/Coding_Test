T = int(input())

for _ in range(T):
    x, y = map(int, input().split())
    n = 1
    while True:
        if (x + n) < (y - 1):
            x += n
            n += 1
        else:
            print(n + 1)
            break
