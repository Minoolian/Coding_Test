N=int(input())
lis=[]

for i in range(N):
    age,name=input().split()
    lis.append([i,int(age),name])

lis.sort(key=lambda x: (x[1],x[0]))

for i in lis:
    print(i[1],i[2])