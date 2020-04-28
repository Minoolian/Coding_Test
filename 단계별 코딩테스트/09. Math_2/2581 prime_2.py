A=int(input());B=int(input())
prime=[]
for n in range(A, B + 1):
    if n==2:
        prime.append(n)
    for i in range(2, n):
        if n % i == 0:
            break
        elif i == n - 1:
            prime.append(n)

if len(prime)==0:
    print(-1)
else:
    print(sum(prime))
    print(prime[0])


# 에라토스테네스의 체(소수거르기) https://pacific-ocean.tistory.com/128?category=810810
# sosu = [0 for i in range(10001)]
# sosu[1] = 1
# for i in range(2, 98):
#     for j in range(i * 2, 10001, i):
#         sosu[j] = 1
# m = int(input())
# n = int(input())
# sum = 0
# min = 0
# for i in range(n, m - 1, -1):
#     if sosu[i] == 0:
#         sum += i
#         min = i
# if sum == 0:
#     print(-1)
# else:
#     print(sum, min, sep='\n')