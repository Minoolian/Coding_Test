# 이상한 피라미드 탐험

#
# https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AWJHmLraeEwDFAUH&categoryId=AWJHmLraeEwDFAUH&categoryType=CODE


import heapq as hq

def dijkstra(start, flag):
    dp[start]=0
    hq.heappush(h,[0, start])

    while h:
        w, n=hq.heappop(h)

        if n==t:
            return dp[t]

        for nn in pyramid[n]:
            if nn>max(m,t):
                continue
            if flag==1 and nn<n:
                continue
            if flag==0 and nn>n:
                continue
            nw=w+1
            if nw<dp[nn]:
                dp[nn]=nw
                hq.heappush(h, [nw, nn])

t=int(input())
for tc in range(1, t+1):
    m, t=map(int,input().split())

    pyramid=[None, [2,3]]
    dp=[100]*(max(m,t)+1)
    h=[]

    num=2
    for i in range(2,450):
        if num>max(m,t):
            break
        for k in range(1, i+1):
            if k==1:
                pyramid.append([num-i+1, num+1, num+i, num+i+1])
            elif k==i:
                pyramid.append([num-i, num-1, num+i, num+i+1])
            else:
                pyramid.append([num-i, num-i+1, num-1, num+1, num+i, num+i+1])
            num+=1
    if m>t: # UP
        flag=0
    else: # DOWN
        flag=1

    print("#{} {}".format(tc,dijkstra(m, flag)))

