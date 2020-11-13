# 박성원

# 서로 다른 정수로 이루어진 집합
# 예를 들어, {5221,40,1,58,9}로 5221401589를 만들 수 있다. 합친수가 정수 K로 나누어 떨어지는 순열
# 박성원이 우연히 정답을 맞출 확률을 분수로 출력

import sys
from math import factorial,gcd

n=int(sys.stdin.readline())
dp=[[0]*101 for _ in range(1<<n)]
# dp[사용여부 bitmask][mod (최대 k=101)]

lis=[]
for _ in range(n):
    lis.append(int(sys.stdin.readline()))

k=int(sys.stdin.readline())

## 모듈러 계산을 위한 준비단계 ##
# "입력받은 수 mod k" 와 이어붙이기 위해 필요한 "10^자릿수 mod k"를 미리 준비.
# ex) A와 B를 붙일 때 => (A*10^(len(B)) + B) mod k
modul_10=[]
for i in range(n):
    modul_10.append(pow(10,len(str(lis[i])))%k)

modul=[]
for i in range(n):
    modul.append(lis[i]%k)
################################

dp[0][0]=1 # 초기설정
for i in range(1<<n): # 모두 돌면서 메모이제이션
    for j in range(k):
        for a in range(n):
            if(i&(1<<a)==0): # 각 수가 포함되어있는지 확인
                m=(j*modul_10[a])%k
                m=(m+modul[a])%k
                dp[i|(1<<a)][m]+=dp[i][j]
                # 수가 포함되어 있지 않다면 포함시킨 것을 메모이제이션

a=dp[(1<<n)-1][0]
b=factorial(n)
g=gcd(a,b) # GCD(최대공약수)로 나누어 기약분수 꼴로 나타낸다.
print(int(a/g),int(b/g),sep="/")

