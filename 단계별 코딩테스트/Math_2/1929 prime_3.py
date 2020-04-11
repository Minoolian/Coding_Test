def prime(num):
    if num==1: return False

    n=int(num**0.5)
    for i in range(2,n+1):
        if num%i==0:
            return False
    return True

M,N=map(int,input().split())
for i in range(M,N+1):
    if prime(i):
        print(i)