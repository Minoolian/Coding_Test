A, B, V = map(int, input().split())
if V <= A:
    print(1)
else:
    if (V - A) % (A - B) == 0:
        # V <= (A-B)*(day-1)+A: 떨어지는 것을 다음날로 취급하여 생각
        print((V - A) // (A - B) + 1)
    else:
        print((V - A) // (A - B) + 2)
