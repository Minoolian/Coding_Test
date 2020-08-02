# 박성원

# 서로 다른 정수로 이루어진 집합
# 예를 들어, {5221,40,1,58,9}로 5221401589를 만들 수 있다. 합친수가 정수 K로 나누어 떨어지는 순열
# 박성원이 우연히 정답을 맞출 확률을 분수로 출력

import sys

n=int(sys.stdin.readline())
lis=[]

for _ in range(n):
    lis.append(int(sys.stdin.readline()))

k=int(sys.stdin.readline())

