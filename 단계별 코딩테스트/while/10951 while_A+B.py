
while True:
    try:
        a, b = map(int, input().split())
        print(a+b)
    except:
        break #input의 갯수가 정해지 않은 경우 예외처리