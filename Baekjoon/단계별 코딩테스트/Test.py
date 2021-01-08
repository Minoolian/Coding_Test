from itertools import permutations

a=[1,2,3]

num=0
for i in permutations(a,3):
    for j in i:
        num=num*10+j

    print(num)
    num=0