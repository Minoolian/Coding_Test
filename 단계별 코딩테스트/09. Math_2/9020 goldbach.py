# 에라토스 테네스의 체
eratos = [True] * 10001

m = int(10001 ** 0.5)
for i in range(2, m + 1):
    if eratos[i] == True:
        for j in range(i + i, 10001, i):
            eratos[j] = False

for _ in range(int(input())):
    N = int(input())
    x= N//2
    for i in range(x,1,-1):
        if eratos[i]==True and eratos[N-i]==True:
            print(i,N-i)
            break


# 더 빠른 식(에라토스테네스의 체) https://pacific-ocean.tistory.com/129?category=810810
# sosu = [0 for i in range(10001)]
# sosu[1] = 1
# for i in range(2, 98):
#     for j in range(i * 2, 10001, i):
#         sosu[j] = 1
# t = int(input())
# for i in range(t):
#     a = int(input())
#     b = a // 2
#     for j in range(b, 1, -1):
#         if sosu[a - j] == 0 and sosu[j] == 0:
#             print(j, a - j)
#             break