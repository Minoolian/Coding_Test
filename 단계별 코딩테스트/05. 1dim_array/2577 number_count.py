a=int(input())
b=int(input())
c=int(input())

mul=str(a*b*c)
array=list(mul)
for i in range(10):
    print(array.count(str(i))) #리스트에서 해당 값의 갯수 계산