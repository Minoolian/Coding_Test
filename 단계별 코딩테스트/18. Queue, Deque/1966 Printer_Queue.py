# 프린터 큐

# 현재 Queue의 가장 앞에 있는 문서의 ‘중요도’를 확인한다.
# 나머지 문서들 중 현재 문서보다 중요도가 높은 문서가 하나라도 있다면, 이 문서를 인쇄하지 않고 Queue의 가장 뒤에 재배치 한다. 그렇지 않다면 바로 인쇄를 한다.

from collections import deque

for _ in range(int(input())):
    n,m=map(int,input().split())
    s=deque(list(map(int,input().split()))) # 우선순위 저장 큐
    check=deque([False for _ in range(n)]) # 찾을 위치 저장 큐
    check[m]=True # 찾을 위치의 값만 True
    cnt=0

    while s:
        if max(s)==s[0]:
            if check[0]==True:
                print(cnt+1)
                break
            s.popleft()
            check.popleft()
            cnt+=1

        else:
            s.append(s.popleft())
            check.append(check.popleft())
