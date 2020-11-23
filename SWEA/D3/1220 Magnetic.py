# Magnetic

# 리스트와 반복문을 이용한 풀이
# https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV14hwZqABsCFAYD&categoryId=AV14hwZqABsCFAYD&categoryType=CODE

for tc in range(1, 11):
    int(input())
    table=[list(map(int,input().split())) for _ in range(100)]

    result=0
    for i in range(100):
        flag=0
        for j in range(100):
            if table[j][i]==1 and flag==0:
                flag=1

            if table[j][i]==2 and flag==1:
                flag=0
                result+=1

    print("#{} {}".format(tc, result))