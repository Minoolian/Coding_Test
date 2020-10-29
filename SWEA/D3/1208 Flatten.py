# Flatten

# 배열을 응용한 풀이.
# https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV139KOaABgCFAYh&categoryId=AV139KOaABgCFAYh&categoryType=CODE&&&

t=int(input())

for tc in range(1, t+1):
    d=int(input())
    h=list(map(int,input().split()))

    for _ in range(d):
        h.sort()
        if h[-1]==h[0]:
            break
        h[-1]-=1
        h[0]+=1

    print("#{} {}".format(tc,max(h)-min(h)))