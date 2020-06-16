# 덱

# push_front X: 정수 X를 덱의 앞에 넣는다.
# push_back X: 정수 X를 덱의 뒤에 넣는다.
# pop_front: 덱의 가장 앞에 있는 수를 빼고, 그 수를 출력한다. 만약, 덱에 들어있는 정수가 없는 경우에는 -1을 출력한다.
# pop_back: 덱의 가장 뒤에 있는 수를 빼고, 그 수를 출력한다. 만약, 덱에 들어있는 정수가 없는 경우에는 -1을 출력한다.
# size: 덱에 들어있는 정수의 개수를 출력한다.
# empty: 덱이 비어있으면 1을, 아니면 0을 출력한다.
# front: 덱의 가장 앞에 있는 정수를 출력한다. 만약 덱에 들어있는 정수가 없는 경우에는 -1을 출력한다.
# back: 덱의 가장 뒤에 있는 정수를 출력한다. 만약 덱에 들어있는 정수가 없는 경우에는 -1을 출력한다.

from collections import deque
import sys

def push_front(x):
    lis.appendleft(x)

def push_back(x):
    lis.append(x)

def pop_front():
    try:
        print(lis.popleft())
    except:
        print(-1)

def pop_back():
    try:
        print(lis.pop())
    except:
        print(-1)

def size():
    return len(lis)

def empty():
    print(1) if size()==0 else print(0)

def front():
    try:
        print(lis[0])
    except:
        print(-1)

def back():
    try:
        print(lis[-1])
    except:
        print(-1)

lis=deque()
for _ in range(int(sys.stdin.readline())):
    cmd=sys.stdin.readline().split()

    if cmd[0]=='push_front':
        push_front(cmd[1])
    elif cmd[0]=='push_back':
        push_back(cmd[1])
    elif cmd[0] == 'pop_front':
        pop_front()
    elif cmd[0] == 'pop_back':
        pop_back()
    elif cmd[0] == 'size':
        print(size())
    elif cmd[0] == 'empty':
        empty()
    elif cmd[0] == 'front':
        front()
    elif cmd[0] == 'back':
        back()