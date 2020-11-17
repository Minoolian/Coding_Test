# Sum

# 리스트를 이용한 풀이.
# https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV13_BWKACUCFAYh&categoryId=AV13_BWKACUCFAYh&categoryType=CODE

for tc in range(1,11):
    n=input()
    lis=[list(map(int,input().split())) for _ in range(100)]
    ver=[0 for _ in range(100)]
    cros=[0 for _ in range(2)]

    result=0
    for i in range(100):
        hor=0
        for j in range(100):
            hor+=lis[i][j]
            ver[j]+=lis[i][j]
            if i==j:
                cros[0]+=lis[i][j]
            if i==99-j:
                cros[1]+=lis[i][j]

        result=max(result, hor)

    print("#{} {}".format(tc,max(result,max(ver),max(cros))))