# 범준이의 제주도 여행 계획

#
# https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=3&problemLevel=4&problemLevel=5&contestProbId=AV4x9oyaCR8DFAUx&categoryId=AV4x9oyaCR8DFAUx&categoryType=CODE&problemTitle=&orderBy=RECOMMEND_COUNT&selectCodeLang=PYTHON&select-1=5&pageSize=30&pageIndex=2

n,m=map(int,input().split())
r=[[None]*n for _ in range(n)]
for i in range(n-1):
    temp=list(map(int,input().split()))
    for j in range(n-1,i,-1):
        rr=temp.pop()
        r[i][j]=rr
        r[j][i]=rr

info=[list(input().split()) for _ in range(n)]

