import random as rand


for _ in range(4):
    lis=[]
    while len(lis)<6:
        a=str(rand.randrange(1,46))
        if a not in lis:
            lis.append(a)

    print(*lis)

