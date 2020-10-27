# N-Queen

# 백트래킹 풀이
# https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV7GKs06AU0DFAXB&categoryId=AV7GKs06AU0DFAXB&categoryType=CODE

def isPromise(x):
    for i in range(x):
        if s[x]==s[i] or abs(s[x]-s[i])==x-i:
            return False
    return True


def dfs(row):
    global n
    global result

    if row>n-1:
        result+=1
    else:
        for i in range(n):
            s[row]=i
            if isPromise(row):
                dfs(row+1)


if __name__=="__main__":
    t=int(input())

    for tc in range(1, t+1):
        n=int(input())
        result=0
        s=[0 for _ in range(n+1)]

        dfs(0)
        print("#{} {}".format(tc,result))