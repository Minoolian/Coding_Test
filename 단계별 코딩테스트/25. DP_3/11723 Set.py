# 집합

# add x: S에 x를 추가한다. (1 ≤ x ≤ 20) S에 x가 이미 있는 경우에는 연산을 무시한다.
# remove x: S에서 x를 제거한다. (1 ≤ x ≤ 20) S에 x가 없는 경우에는 연산을 무시한다.
# check x: S에 x가 있으면 1을, 없으면 0을 출력한다. (1 ≤ x ≤ 20)
# toggle x: S에 x가 있으면 x를 제거하고, 없으면 x를 추가한다. (1 ≤ x ≤ 20)
# all: S를 {1, 2, ..., 20} 으로 바꾼다.
# empty: S를 공집합으로 바꾼다

import sys

t=int(sys.stdin.readline())
S=0

def add(S): # shift, or 연산자로 1로 변환
    S |= 1 << int(cmd[1])
    return S

def remove(S): # shift+not , and 연산자로 0으로 변환
    S &= ~(1 << int(cmd[1]))
    return S

def check(S): # shift, and 연산자로 확인
    if S & (1 << int(cmd[1])):
        return 1
    else:
        return 0

while t:
    t-=1
    cmd=sys.stdin.readline().split()

    if cmd[0] == "add":
        S=add(S)

    if cmd[0] == "remove":
        S=remove(S)

    if cmd[0] == "check":
        print(check(S))

    if cmd[0] == "toggle":
        if check(S):
            S=remove(S)
        else:
            S=add(S)
    # S ^= 1<<(int(cmd[1]))
    # XOR 연산자로 Toggle 가능

    if cmd[0] == "all":
        S=(1<<21)-1
    if cmd[0] == "empty":
        S=0