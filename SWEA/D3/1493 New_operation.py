# 수의 새로운 연산

# 반복문과 리스트의 활용
# https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV2b-QGqADMBBASw&categoryId=AV2b-QGqADMBBASw&categoryType=CODE

tmp=[[0,0] for i in range(1000001)]

st=1
for i in range(1,301):
    num=st
    plus=i+1
    for j in range(1,301):
        tmp[num]=[j,i]
        num+=plus
        plus+=1
    st+=i

t=int(input())
for tc in range(1, t+1):
    p,q=map(int,input().split())

    x1,y1=tmp[p]
    x2,y2=tmp[q]

    for a in range(1000001):
        x,y=tmp[a]
        if x1+x2==x and y1+y2==y:
            print("#{} {}".format(tc,a))
            break
