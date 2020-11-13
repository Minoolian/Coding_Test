# 계수정렬, 최대값 만큼의 배열을 만들어 갯수를 센 후, 작은값 부터 출력해준다.
import sys

N=int(input())
lis=[0]*10001

for i in range(N):
    lis[int(sys.stdin.readline())]+=1
for i in range(10001):
    if lis[i]!=0:
        for j in range(lis[i]):
            print(i)