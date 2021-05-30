# 조합

# 페르마의 소정리 및 팩토리얼을 쪼개는 방법
# https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=3&problemLevel=4&problemLevel=5&contestProbId=AWXGKdbqczEDFAUo&categoryId=AWXGKdbqczEDFAUo&categoryType=CODE&problemTitle=&orderBy=SUBMIT_COUNT&selectCodeLang=PYTHON&select-1=5&pageSize=30&pageIndex=1

def solve(a,b):
    if b==0:
        return 1
    elif b==1:
        return a
    elif b%2==0:
        return pow(solve(a,b//2),2)%p
    elif b%2==1:
        return pow(solve(a,b//2),2)*a%p

t=int(input())
for tc in range(1,t+1):
    n,k=map(int,input().split())

    a=1; b=1; p=1234567891

    for i in range(1,n+1):
        a*=i ; a%=p
    for i in range(1,k+1):
        b*=i ; b%=p
    for i in  range(1,n-k+1):
        b*=i ; b%=p

    b=solve(b,p-2)

    print(f"#{tc} {(a*b)%p}")