# 농작물 수확하기

# 반복문 풀이.
# https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV7GLXqKAWYDFAXB&categoryId=AV7GLXqKAWYDFAXB&categoryType=CODE

t=int(input())

for tc in range(1, t+1):
    n=int(input())
    lis=[list(map(int,input())) for _ in range(n)]

    mid=n//2

    result=0
    for i in range(mid+1):
        for j in range(mid-i,mid+i+1):
            result+=lis[i][j]
            if i!=mid:
                result+=lis[n-1-i][j]

    print("#{} {}".format(tc, result))