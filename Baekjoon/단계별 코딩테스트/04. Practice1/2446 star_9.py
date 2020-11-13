# 별찍기 문제는 나누어서 생각하는 연습이 필요.
n=int(input())

for i in range(1,n+1):
    print(" "*(i-1)+"*"*((2*n-1)-2*(i-1)))

for i in range(1,n):
    print(" "*(n-i-1)+"*"*(2*i+1))

