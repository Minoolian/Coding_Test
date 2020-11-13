N=int(input())

lis= [list(map(int,input().split())) for _ in range(N)]

lis=sorted(lis,key=lambda x:(x[0],x[1]))

for i in lis:
    print(i[0],i[1])