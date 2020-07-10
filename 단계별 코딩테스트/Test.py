lis=[[list(map(int,input().split())) for _ in range(3)]]*2

for a in lis:
    for b in a:
        if 0 in b:
            print(0)
            exit(0)