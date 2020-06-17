# 회전하는 큐

# 첫 번째 원소를 뽑아낸다. 이 연산을 수행하면, 원래 큐의 원소가 a1, ..., ak이었던 것이 a2, ..., ak와 같이 된다.
# 왼쪽으로 한 칸 이동시킨다. 이 연산을 수행하면, a1, ..., ak가 a2, ..., ak, a1이 된다.
# 오른쪽으로 한 칸 이동시킨다. 이 연산을 수행하면, a1, ..., ak가 ak, a1, ..., ak-1이 된다.
# 그 원소를 주어진 순서대로 뽑아내는데 드는 2번, 3번 연산의 최솟값

from collections import deque

n,m = map(int,input().split())
q=deque([i for i in range(1,n+1)])

loc=list(map(int,input().split()))
cnt=0

for i in loc:
    if q.index(i)<=len(q)//2:
        while True:
            if i!=q[0]:
                q.append(q.popleft())
                cnt+=1
            else:
                q.popleft()
                break
    else:
        while True:
            if i!=q[0]:
                q.appendleft(q.pop())
                cnt+=1
            else:
                q.popleft()
                break

print(cnt)