# 이상한 피라미드 탐험

# BFS를 이용한 풀이
# https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AWJHmLraeEwDFAUH&categoryId=AWJHmLraeEwDFAUH&categoryType=CODE


from collections import deque

def bfs(start):
    q.append(start)

    while q:
        n=q.popleft()

        if n==t:
            return dp[t]

        for nn in pyramid[n]:
            if nn>t:
                continue
            if visit[nn] :
                q.append(nn)
                visit[nn]=False
                dp[nn]=dp[n]+1


pyramid=[None, [2,3]]
num=2
for i in range(2,150):
    if num>10000:
        break
    for k in range(1, i+1):
        if k==1:
            pyramid.append([num-i+1, num+1, num+i, num+i+1])
        elif k==i:
            pyramid.append([num-i, num-1, num+i, num+i+1])
        else:
            pyramid.append([num-i, num-i+1, num-1, num+1, num+i, num+i+1])
        num+=1

t=int(input())
for tc in range(1, t+1):
    m, t=map(int,input().split())
    if m>t:
        m, t=t, m

    dp=[0]*(t+1)
    visit=[True]*(t+1)
    q=deque()

    print("#{} {}".format(tc,bfs(m)))

