N = int(input())
x = 2
re = 1

if N == 1:
    print(1)
else:
    while True:
        if N >= x and N < x + 6 * re:
            # 방의 갯수가 같은 수가 6n 의 범위에 속해있다.
            print(re + 1)
            break
        else:
            x += 6 * re
            re += 1