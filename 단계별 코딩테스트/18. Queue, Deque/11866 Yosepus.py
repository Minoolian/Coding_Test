# 요세푸스 문제 0

# 1번부터 N번까지 N명의 사람이 원을 이루면서 앉아있고, 양의 정수 K(≤ N)가 주어진다.
# 이제 순서대로 K번째 사람을 제거한다. 한 사람이 제거되면 남은 사람들로 이루어진 원을 따라 이 과정을 계속해 나간다.
# 이 과정은 N명의 사람이 모두 제거될 때까지 계속된다. 원에서 사람들이 제거되는 순서를 (N, K)-요세푸스 순열이라고 한다.

from collections import deque

n, k=map(int, input().split())
q=deque([i for i in range(1,n+1)])
result=[]

while q:
    for _ in range(k-1):
        q.append(q.popleft())
    result.append(q.popleft())

print("<",end="")
for i in range(len(result)):
    if i == len(result)-1:
        print(result[i], end="")
    else:
        print(result[i],end=", ")
print(">")



