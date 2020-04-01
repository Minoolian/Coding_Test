#몫 q(quotient) 냐머지 r(remainder, modulo)
a=[]
for i in range(10):
    a.append(int(input())%42)

a=list(set(a)) #중복을 제거해주는 집합자료형 set
print(len(a))