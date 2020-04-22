person=[]

for _ in range(int(input())):
    person.append(list(map(int,input().split())))

for x in person:
    rank=1
    for y in person:
        if x==y:
            continue
        else:
            if x[0]<y[0] and x[1]<y[1]:
                rank+=1
            else:
                continue
    print(rank,end=" ")
