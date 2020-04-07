st=input()
list=["ABC","DEF","GHI","JKL","MNO","PQRS","TUV","WXYZ"]
ret=0

for i in st:
    for j in list:
        if i in j:
            ret+=list.index(j)+3

print(ret)