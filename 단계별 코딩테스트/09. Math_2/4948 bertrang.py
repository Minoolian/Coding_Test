# 에라토스 테네스의 체
def prime(num):

    eratos=[True]*num

    m=int(num**0.5)
    for i in range(2,m+1):
        if eratos[i]==True:
            for j in range(i+i,num,i):
                eratos[j]=False
    return [i for i in range(2,num) if eratos[i]==True]

while True:
    N = int(input())
    if N==0:
        break
    li=prime(2*N+1) # 1~n 까지의 소수 리스트 반환
    print(len([i for i in li if i>N])) #리스트 내포 (n ~ 2n 까지 걸름)
