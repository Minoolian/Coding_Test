# 일부 작은 조각이 전체와 비슷한 기하학적 형태로 나타는 프랙탈.
def star(x,y,n):
    if n==1:
        S[x][y]='*'
        return

    nn=n//3
    for i in range(3):
        for j in range(3):
            if i==1 and j==1: # 구멍을 낼 부분은 스킵.
                continue
            star(x+nn*i,y+nn*j,nn)

N=int(input())
S=[[" " for i in range(N)] for j in range(N)]
star(0,0,N)
for i in range(N):
    for j in range(N):
        print(S[i][j],end="")
    print("")


# join, zip 을 이용한 방법 (시간이 매우 짧다)
# def concatenate(r1, r2):
#     return [''.join(x) for x in zip(r1, r2, r1)]
#
#
# def star10(n):
#     if n == 1:
#         return ['*']
#     n //= 3
#     x = star10(n)
#     a = concatenate(x, x)
#     b = concatenate(x, [' ' * n] * n)
#
#     return a + b + a
#
#
# print('\n'.join(star10(int(input()))))