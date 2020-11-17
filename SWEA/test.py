from collections import deque

a=[[1,2],[2,3]]
q=deque()
q.append([1,2])
q.append([1,1])
a=deque(a)
print(a)