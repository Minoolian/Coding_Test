# 검문

# 숫자 N개를 종이에 적는다. 그 다음, 종이에 적은 수를 M으로 나누었을 때, 나머지가 모두 같게 되는 M을 모두 찾으려고 한다.
# M은 1보다 커야 한다.
# N개의 수가 주어졌을 때, 가능한 M을 모두 찾아라.

import math

n=int(input())
num=[int(input()) for _ in range(n)]
m=[]

gcd=num[1]-num[0]
for i in range(1,n):
    gcd=math.gcd(abs(num[i]-num[i-1]),gcd)

# n[0]=q[0]*m+r
# n[1]=q[1]*m+r
# n[2]=q[2]*m+r
# n[i]-n[i-1]=(q[i]-q[i-1])*m
# 즉 m에 들어갈 수 있는 후보군들은 n[i]-n[i-1]의 약수들.
# n[1]-n[0] 의 약수, n[2]-n[1] 의 약수 중 공통된 것 => 최대공약수의 약수들
# 이렇게 쭉 간추려 가면 된다.

for i in range(2, int(math.sqrt(gcd))+1):
    if gcd%i ==0:
        m.append(i)
        m.append(gcd//i)

# 2 ~ n까지 모두 검사할 수 있지만, 에라토스테네스의 체에서 했듯 효율적이지 않으므로, 2~sqrt(n) 까지 검사한다.
# 약수의 절반은 2~sqrt(n) 으로 판별할 수 있으므로, 나머지 절반은 n//약수 를 나눈 것으로 구할 수 있다.

m.append(gcd)
m=list(set(m))
m.sort()
for i in m:
    print(i, end=' ')



