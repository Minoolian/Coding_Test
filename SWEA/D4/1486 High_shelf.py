# 장훈이의 높은 선반

# DFS를 이용한 풀이
# https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV2b7Yf6ABcBBASw&categoryId=AV2b7Yf6ABcBBASw&categoryType=CODE


def dfs(idx,chk):
    global result
    if chk>=b:
        result=min(result,chk)
        return
    else:
        for i in range(idx+1, n):
            dfs(i,chk+h[i])

if __name__=="__main__":
    t=int(input())

    for tc in range(1, t+1):
        n,b=map(int,input().split())
        h=list(map(int,input().split()))
        result=float('inf')
        dfs(-1,0)
        print("#{} {}".format(tc,result-b))