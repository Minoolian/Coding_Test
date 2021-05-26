# 범준이의 제주도 여행 계획

# dfs를 이용한 풀이
# https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=3&problemLevel=4&problemLevel=5&contestProbId=AV4x9oyaCR8DFAUx&categoryId=AV4x9oyaCR8DFAUx&categoryType=CODE&problemTitle=&orderBy=RECOMMEND_COUNT&selectCodeLang=PYTHON&select-1=5&pageSize=30&pageIndex=2


def dfs(cur,t,d,m,s,visit,result):
    global fin

    if d<m:
        for i in range(1,n+1):
            if info[i][0]=='A':
                continue
            if visit[i] and cur!=i:
                if info[i][0]=='H' and t-r[cur][i]>=0:
                    dfs(i, 540, d+1, m, s, visit, result+[i])
                elif info[i][0]!='H' and t-r[cur][i]-int(info[i][1])>=10:
                    visit[i]=False
                    dfs(i, t-r[cur][i]-int(info[i][1]), d, m, s+int(info[i][2]), visit, result+[i])
                    visit[i]=True
    else:
        for i in range(1,n+1):
            if info[i][0]=='H':
                continue
            if visit[i] and cur!=i:
                if info[i][0]=='A' and t-r[cur][i]>=0:
                    if (fin[0]==s and len(fin[1])<len(result+[i])) or fin[0]<s:
                        fin=[s,result+[i]]

                elif info[i][0]!='A' and t-r[cur][i]-int(info[i][1])>=10:
                    visit[i]=False
                    dfs(i, t-r[cur][i]-int(info[i][1]), d, m, s+int(info[i][2]), visit, result+[i])
                    visit[i]=True

n=int(input())
for tc in range(1,n+1):
    n,m=map(int,input().split())
    r=[[None]*(n+1) for _ in range(n+1)]
    for i in range(n-1):
        temp=list(map(int,input().split()))
        for j in range(n-1,i,-1):
            rr=temp.pop()
            r[i+1][j+1]=rr
            r[j+1][i+1]=rr

    info=[None]+[list(input().split()) for _ in range(n)]
    visit=[True]*(n+1)
    fin=[0,[]]

    dfs(1,540,1,m,0,visit,[])
    print(fin)

