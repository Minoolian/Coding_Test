# 보급로

# Dijkstra 알고리즘 풀이.
# https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV15QRX6APsCFAYD&categoryId=AV15QRX6APsCFAYD&categoryType=CODE

import heapq as hq

def dijkstra(a,b):
    h=[]
    hq.heappush(h,[0,a,b])

    idx_x=[1,0,-1,0]
    idx_y=[0,1,0,-1]

    while h:
        w,x,y=hq.heappop(h)

        for i in range(4):
            n_x=x+idx_x[i]
            n_y=y+idx_y[i]

            if n_x<n and n_x>=0 and n_y<n and n_y>=0:
                n_w=lis[n_x][n_y]+w
                if dp[n_x][n_y]>n_w:
                    dp[n_x][n_y]=n_w
                    hq.heappush(h,[n_w,n_x,n_y])

if __name__=="__main__":

    t=int(input())

    for tc in range(1,t+1):
        n=int(input())
        lis=[list(map(int,input())) for _ in range(n)]
        dp=[[float('inf')]*n for _ in range(n)]

        dijkstra(0,0)
        print("#{} {}".format(tc, dp[n-1][n-1]))