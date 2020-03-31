a=int(input())
count=0
new=a

while True:
    count+=1

    remain=new%10
    quote=new//10 #몫을 계산하는 // 연산자

    sum=remain+quote
    sum=sum%10
    new=int(str(remain)+str(sum))
    #또는 remain*10 을 하여 두 수를 더해도 된다.

    if a==new:
        print(count)
        break