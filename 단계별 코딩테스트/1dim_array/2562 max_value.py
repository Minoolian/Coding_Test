a=[]
for i in range(9):
    a.append(int(input()))
print(max(a))
print(a.index(max(a))+1) #리스트에서 해당 값의 인덱스 반환