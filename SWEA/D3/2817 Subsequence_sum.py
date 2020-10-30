# 부분 수열의 합

# DFS(백트래킹)를 이용한 전체탐색 풀이.
# https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV7IzvG6EksDFAXB&categoryId=AV7IzvG6EksDFAXB&categoryType=CODE

def dfs(idx,chk):
    global result
    if chk==k:
        result+=1

    elif chk>k: return
    else:
        for i in range(idx+1, n):
            dfs(i,chk+lis[i])

if __name__=="__main__":
    t=int(input())

    for tc in range(1, t+1):
        n,k=map(int,input().split())
        lis=list(map(int,input().split()))
        result=0
        dfs(-1,0)
        print("#{} {}".format(tc,result))