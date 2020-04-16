
while True:
    x = list(map(int, input().split()))
    if sum(x)==0:
        break
    x.sort() # 영구 정렬
    if x[2] ** 2 == x[1] ** 2 + x[0] ** 2:
        print("right")
    else:
        print("wrong")