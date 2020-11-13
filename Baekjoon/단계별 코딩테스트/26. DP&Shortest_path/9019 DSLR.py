# DSLR

# n의 네 자릿수를 d1, d2, d3, d4

# D: D 는 n을 두 배로 바꾼다. 결과 값이 9999 보다 큰 경우에는 10000 으로 나눈 나머지를 취한다. 그 결과 값(2n mod 10000)을 레지스터에 저장한다.
# S: S 는 n에서 1 을 뺀 결과 n-1을 레지스터에 저장한다. n이 0 이라면 9999 가 대신 레지스터에 저장된다.
# L: L 은 n의 각 자릿수를 왼편으로 회전시켜 그 결과를 레지스터에 저장한다. 이 연산이 끝나면 레지스터에 저장된 네 자릿수는 왼편부터 d2, d3, d4, d1이 된다.
# R: R 은 n의 각 자릿수를 오른편으로 회전시켜 그 결과를 레지스터에 저장한다. 이 연산이 끝나면 레지스터에 저장된 네 자릿수는 왼편부터 d4, d1, d2, d3이 된다.

# A에서 B로 변환하기 위해 필요한 최소한의 명령어 나열을 출력

import sys
from collections import deque

T=int(sys.stdin.readline())

while T:
    T-=1

    a,b=map(int,sys.stdin.readline().split())
    check=[0 for _ in range(10000)]

    q=deque()
    q.append([a,""])

    while q:
        num, cmd=q.popleft()

        if num==b:
            print(cmd)
            break

        D=(2*num)%10000
        if check[D]==0:
            check[D]=1
            q.append([D, cmd+"D"])

        S=num-1 if num!=0 else 9999
        if check[S]==0:
            check[S]=1
            q.append([S, cmd+"S"])

        L=num%1000*10 + num//1000
        if check[L]==0:
            check[L]=1
            q.append([L, cmd+"L"])

        R=num%10*1000 + num//10
        if check[R]==0:
            check[R]=1
            q.append([R, cmd+"R"])

