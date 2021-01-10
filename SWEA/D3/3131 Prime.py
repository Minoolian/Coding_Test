# 100만 이하의 모든 소수

# 에라토스테네스의 체를 이용한 풀이.
# https://swexpertacademy.com/main/code/problem/problemList.do?problemLevel=3&problemLevel=4&problemLevel=5&problemTitle=&orderBy=RECOMMEND_COUNT&selectCodeLang=PYTHON&select-1=5&pageSize=30&pageIndex=2#none

sosu = [0 for i in range(1000001)]
sosu[1] = 1

m=int(1000000**0.5)
for i in range(2, m+1):
    for j in range(i * 2, 1000001, i):
        sosu[j] = 1

for i in range(2,1000001):
    if sosu[i] == 0:
        print(i,end=" ")
