n=int(input())
for i in range(n):
    a=list(map(int,input().split()))
    ave=(sum(a)-a[0])/a[0] # slice를 이용해서 a[1:]이 효율적
    count=0

    for i in range(1,len(a)): # 또한 range a[1:]
        if a[i]>ave:
            count+=1

    print("%.3f%%"%(count/a[0]*100))
