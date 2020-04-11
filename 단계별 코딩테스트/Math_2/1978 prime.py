N=int(input())
A=list(map(int,input().split()))
count=len(A)

for j in A:
    if j==1:
        count-=1
    for i in range(2,j):
        if j%i==0:
            count -= 1
            break
print(count)