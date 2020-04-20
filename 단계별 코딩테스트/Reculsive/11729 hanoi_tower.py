
n = int(input())
def hanoi(n, a, b, c):
    if n == 1:
        print(a, c)
    else:
        hanoi(n - 1, a, c, b) # n-1 개의 원판을 1 -> 2로 이동.
        print(a, c) # 맨밑의 원판을 1 -> 3으로 이동
        hanoi(n - 1, b, a, c) # 2에 있는 n-1개의 원판을 3으로 이동
sum = 1
for i in range(n - 1):
    sum = sum * 2 + 1 # 하노이 타워의 이동 횟수는 2^n-1
print(sum)
hanoi(n, 1, 2, 3)