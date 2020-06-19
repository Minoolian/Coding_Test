# 곱셈

# 자연수 A를 B번 곱한 수를 알고 싶다. 단 구하려는 수가 매우 커질 수 있으므로 이를 C로 나눈 나머지를 구하는 프로그램
# 첫째 줄에 A를 B번 곱한 수를 C로 나눈 나머지를 출력한다.
import math

a,b,c=map(int,input().split())

def solve(a,b): # 단순한 방법으로는 너무 큰 수를 다루므로, A^50 = (A^25)^2 = ((A^12)^2*A)^2 등으로 나누어 풀이
    if b==0:
        return 1
    elif b==1:
        return a
    elif b%2==0:
        return pow(solve(a,b//2),2)%c # modulo 연산의 속성 (a*b) mod c =(a mod c * b mod c) mod c
    elif b%2==1:
        return pow(solve(a,b//2),2)*a%c

print(solve(a,b)%c)