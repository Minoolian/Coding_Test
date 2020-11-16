# 최적경로

# 비트마스크를 이용한 TSP 응용문제
# https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV15OZ4qAPICFAYD&categoryId=AV15OZ4qAPICFAYD&categoryType=CODE&&&

def dist(a,b):
    return abs(a[0]-b[0]) + abs(a[1]-b[1])

def tsp(cur, visited):
    if visited==(1<<n+1)-1:
        return dist(idx[cur],idx[-1])

    if dp[cur][visited]!=None:
        return dp[cur][visited]

    temp=inf
    for custom in range(n+1):
        if visited & (1<<custom)==0:
            temp=min(temp, dist(idx[cur], idx[custom]) + tsp(custom, visited | (1<<custom)))
    dp[cur][visited]=temp
    return temp

t=int(input())
for tc in range(1, t+1):
    inf=float('inf')
    n=int(input())
    lis=list(map(int,input().split()))
    idx=[]
    idx.append([lis[0],lis[1]]) # 회사좌표
    for i in range(2,n+2):
        idx.append([lis[2*i],lis[2*i+1]])
    idx.append([lis[2],lis[3]]) # 집좌표

    dp=[[None]*(1<<n+1) for _ in range(n+1)]

    print("#{} {}".format(tc,tsp(0, 1<<0)))