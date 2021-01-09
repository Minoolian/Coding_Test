# 100만 이하의 모든 소수

#
# https://swexpertacademy.com/main/code/problem/problemList.do?problemLevel=3&problemLevel=4&problemLevel=5&problemTitle=&orderBy=RECOMMEND_COUNT&selectCodeLang=PYTHON&select-1=5&pageSize=30&pageIndex=2#none

sosu = [0 for i in range(1000001)]
sosu[1] = 1
for i in range(2, 98):
    for j in range(i * 2, 1000001, i):
        sosu[j] = 1
m = int(input())
n = int(input())
sum = 0
min = 0
for i in range(n, m - 1, -1):
    if sosu[i] == 0:
        sum += i
        min = i
if sum == 0:
    print(-1)
else:
    print(sum, min, sep='\n')