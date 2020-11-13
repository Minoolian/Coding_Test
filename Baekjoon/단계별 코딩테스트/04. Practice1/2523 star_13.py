# https://hellominchan.tistory.com/108
# N = int(input())
#
# for i in range(1, N + 1):
#     for j in range(i):
#         print("*", end="")
#     print()
#
# for i in range(N - 1, 0, -1):
#     for j in range(i):
#         print("*", end="")
#     print()

#https://cleancode-ws.tistory.com/m/31?category=796110
a = int(input())
b = a

for k in range(1, b + 1):
    print('*' * (k))

for i in range(1, a):
    print('*' * (b - i))