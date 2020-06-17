# AC

# 함수 R은 배열에 있는 숫자의 순서를 뒤집는 함수이고, D는 첫 번째 숫자를 버리는 함수이다. 배열이 비어있는데 D를 사용한 경우에는 에러가 발생
#
# 첫째 줄에 테스트 케이스의 개수 T
# 각 테스트 케이스의 첫째 줄에는 수행할 함수 p
# 다음 줄에는 배열에 들어있는 수의 개수 n
# 다음 줄에는 [x1,...,xn]과 같은 형태로 배열에 들어있는 수

from collections import deque
import sys

for _ in range(int(sys.stdin.readline())):
    p=sys.stdin.readline()
    n=int(sys.stdin.readline())
    lis=list(sys.stdin.readline().rstrip()[1:-1].split(","))

    e=0
    head=0
    tail=len(lis)-1
    direction=True

    for i in p:
        try:
            if i=='R':
                if direction==True:
                    direction=False
                else:
                    direction=True

            elif i=='D':
                if n!=0:
                    if direction==True:
                        head+=1
                    else:
                        tail-=1
                    n-=1
                else:
                    print("error")
                    e=1
                    break
        except:
            print("error")
            e=1
            break

    if e==0:
        if direction==True:
            print('['+','.join(lis[head:tail+1])+']')
        else:
            if head==0:
                print('[' + ','.join(lis[tail::-1]) + ']')
            else:
                print('[' + ','.join(lis[tail:head-1:-1]) + ']')

