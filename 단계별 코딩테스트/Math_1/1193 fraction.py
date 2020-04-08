
N = int(input())
x, a = 1, 1

while True:
    if N < x + a: # a는 해당층수, if (층수의 경계 안에 해당되면)
        gap = N - x # 홀수층, 짝수층에 따라 gap으로 값이 나뉨
        if a % 2 == 0:
            print(1 + gap, "/", a - gap,sep="")
        else:
            print(a - gap, "/", gap + 1,sep="")
        break
    else:
        x = x + a
        a += 1
        

