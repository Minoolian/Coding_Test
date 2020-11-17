# 자기 방으로 돌아가기

# 그리디 풀이.
# https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AWNcJ2sapZMDFAV8&categoryId=AWNcJ2sapZMDFAV8&categoryType=CODE

from collections import deque

t=int(input())

for tc in range(1, t+1):
    n=int(input())
    q=[]
    for _ in range(n):
        a,b=map(int,input().split())
        if a>b:
            a,b = b,a
        q.append([a,b])
    q.sort(key=lambda x:(x[0],x[1]))
    q=deque(q)
    result=0
    while q:
        l=len(q)
        room=0
        for _ in range(l):
            s,e=q.popleft()

            if not s%2: ns=s-1
            else: ns=s

            if ns>room:
                if not e%2: ne=e
                else: ne=e+1
                room=ne
            else:
                q.append([s,e])
        result+=1

    print("#{} {}".format(tc,result))