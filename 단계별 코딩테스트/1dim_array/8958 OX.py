n=int(input())
for i in range(n):
    a=list(input())
    sum=0
    count=0
    for i in range(len(a)):
        if a[i]=='O':
            count+=1
            sum+=count
        else:
            count=0
    print(sum)