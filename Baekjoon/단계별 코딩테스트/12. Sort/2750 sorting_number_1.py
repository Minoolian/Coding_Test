# 버블정렬
N=int(input())
number=[]
for _ in range(N):
    number.append(int(input()))

for i in range(N):
    for j in range(N-i-1):
        if number[j]>number[j+1]:
            number[j], number[j+1] = number[j+1], number[j] # 파이썬 자리바꾸기

for j in range(N):
    print(number[j])
