# 팩토리얼 0의 갯수

# N!에서 뒤에서부터 처음 0이 아닌 숫자가 나올 때까지 0의 갯수를 구하라.

from math import factorial

n=factorial(int(input()))
result=0

while n%10==0:
       n=n//10
       result+=1

print(result)
# 이 방법 외에도 뒤에 0의 갯수는 5, 10을 곱했을 때 0이 증가한다.