# 스택

# push X: 정수 X를 스택에 넣는 연산이다.
# pop: 스택에서 가장 위에 있는 정수를 빼고, 그 수를 출력한다. 만약 스택에 들어있는 정수가 없는 경우에는 -1을 출력한다.
# size: 스택에 들어있는 정수의 개수를 출력한다.
# empty: 스택이 비어있으면 1, 아니면 0을 출력한다.
# top: 스택의 가장 위에 있는 정수를 출력한다. 만약 스택에 들어있는 정수가 없는 경우에는 -1을 출력한다.

import sys # 시간 초과로 인한 sys 모듈 사용

def push(n):
    lis.append(n)

def pop():
    try:
        print(lis.pop())
    except:
        print(-1)

def size():
    return len(lis)

def empty():
    a=1 if size()==0 else 0 # 새로 알게된 if 구문.
    print(a)

def top():
    try:
        print(lis[-1])
    except:
        print(-1)


a=int(sys.stdin.readline())
lis=[]
for _ in range(a):
    cmd=sys.stdin.readline().split()
    if cmd[0]=='push':
        push(cmd[1])
    elif cmd[0]=='pop':
        pop()
    elif cmd[0] =='size':
        print(size())
    elif cmd[0]=='empty':
        empty()
    elif cmd[0] == 'top':
        top()
