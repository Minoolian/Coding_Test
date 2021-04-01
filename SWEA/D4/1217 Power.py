# 거듭제곱

# 재귀호출을 이용한 풀이
# https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV14dUIaAAUCFAYD&categoryId=AV14dUIaAAUCFAYD&categoryType=CODE


def power(n,m):
    if m==1:
        return n
    return power(n,m-1)*n

for tc in range(1,11):
    input()
    n,m=map(int,input().split())
    print("#{} {}".format(tc,power(n,m)))