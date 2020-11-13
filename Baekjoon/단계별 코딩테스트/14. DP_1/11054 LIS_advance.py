# 가장 긴 바이토닉 부분 수열

# 수열 S가 어떤 수 Sk를 기준으로 S1 < S2 < ... Sk-1 < Sk > Sk+1 > ... SN-1 > SN을 만족한다면, 그 수열을 바이토닉 수열이라고 한다.
# 예를 들어, {10, 20, 30, 25, 20}과 {10, 20, 30, 40}, {50, 40, 25, 10} 은 바이토닉 수열이지만,  {1, 2, 3, 2, 1, 2, 3, 2, 1}과 {10, 20, 30, 40, 20, 30} 은 바이토닉 수열이 아니다.

import sys

n=int(sys.stdin.readline())
lis=list(map(int,sys.stdin.readline().split()))

forward=[1 for _ in range(n)]
reverse=[1 for _ in range(n)]
result=[]

# 기존 LIS를 수행한다.
for i in range(n):
    for j in range(i):
        if lis[i] > lis[j]:
            forward[i]=max(forward[i],forward[j]+1)
lis.reverse()

# 리스트를 뒤집어 LIS를 수행한다.
for i in range(n):
    for j in range(i):
        if lis[i] > lis[j]:
            reverse[i]=max(reverse[i],reverse[j]+1)
# 뒤집은 LIS의 결과를 다시 뒤집는다.
# 그럼 역으로 수행한 LIS의 결과가 정방향으로 저장된다.
reverse.reverse()

# 정방향 LIS와 역방향 LIS의 합이 원하는 바이토닉 부분 수열이다.
for i in range(n):
    result.append(forward[i]+reverse[i])

# 해당 가운데 값은 제외하고 결과를 계산한다.
print(max(result)-1)