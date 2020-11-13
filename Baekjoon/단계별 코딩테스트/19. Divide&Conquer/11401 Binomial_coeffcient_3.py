# 이항 계수 3

# 자연수n 과 정수k 가 주어졌을 때 이항 계수 를 1,000,000,007로 나눈 나머지

# 페르마의 소정리: a^p-1 mod p = 1 따라서 a^p-2 mod p = a^-1
# A=n! , B=k!(n-k)! , nCk = A/B
# (A*B^-1) mod p = ((A mod p) * (B^-1 mod p)) mod p
# = ((A mod p) * (B^p-2 mod p)) mod p
# 이유는 모듈러의 곱셈 성질은 나눗셈에는 적용되지 않는다.
# 단순히 정의만을 이용해서 풀기에는 오버플로우 문제가 있기에 모듈러 성질을 이용한다.




def solve(a,b): # 단순한 방법으로는 너무 큰 수를 다루므로, A^50 = (A^25)^2 = ((A^12)^2*A)^2 등으로 나누어 풀이
    if b==0:
        return 1
    elif b==1:
        return a
    elif b%2==0:
        return pow(solve(a,b//2),2)%p # modulo 연산의 속성 (a*b) mod c =(a mod c * b mod c) mod c
    elif b%2==1:
        return pow(solve(a,b//2),2)*a%p

n, k=map(int, input().split())

a=1
b=1
p=1000000007

for i in range(1,n+1):
    a*=i ; a%=p
for i in range(1,k+1):
    b*=i ; b%=p
for i in  range(1,n-k+1):
    b*=i ; b%=p

b=solve(b,p-2)%p
result=(a*b)%p
print(result)

