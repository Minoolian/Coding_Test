#큐 2

# push X: 정수 X를 큐에 넣는 연산이다.
# pop: 큐에서 가장 앞에 있는 정수를 빼고, 그 수를 출력한다. 만약 큐에 들어있는 정수가 없는 경우에는 -1을 출력한다.
# size: 큐에 들어있는 정수의 개수를 출력한다.
# empty: 큐가 비어있으면 1, 아니면 0을 출력한다.
# front: 큐의 가장 앞에 있는 정수를 출력한다. 만약 큐에 들어있는 정수가 없는 경우에는 -1을 출력한다.
# back: 큐의 가장 뒤에 있는 정수를 출력한다. 만약 큐에 들어있는 정수가 없는 경우에는 -1을 출력한다.

# O(1) 의 시간복잡도를 가지게 구성해야한다.
# pop(0)의 경우 O(n)의 시간복잡도를 요구한다.

# Collection 모듈의 Deque 를 사용하는 방법도 있다.

import sys

check=0 # pop 할 경우 head를 이동하여 O(1) 구성

def push(x):
    lis.append(x)

def pop():
    global check

    if check < len(lis):
        print(lis[check])
        check+=1
    else:
        print(-1)

def size():
    return len(lis)-(check)

def empty():
    print(1) if size()==0 else print(0)

def front():
    if check < len(lis):
        print(lis[check])
    else:
        print(-1)

def back():
    if check < len(lis):
        print(lis[-1])
    else:
        print(-1)

lis=[]
n=int(sys.stdin.readline())
for _ in range(n):
    cmd=sys.stdin.readline().split()
    if cmd[0]=='push':
        push(cmd[1])
    elif cmd[0]=='pop':
        pop()
    elif cmd[0] =='size':
        print(size())
    elif cmd[0]=='empty':
        empty()
    elif cmd[0] == 'front':
        front()
    elif cmd[0] == 'back':
        back()