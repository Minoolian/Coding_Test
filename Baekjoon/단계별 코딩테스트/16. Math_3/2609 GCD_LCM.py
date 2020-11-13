# 최대공약수(Greatest Common Divisor)와 최소공배수(Least Common Multiple)

a,b = map(int,input().split())
A,B = a,b

while b!=0:
    a = a%b
    a,b=b,a

print(a) # GCD
print(A*B//a) # LCM
