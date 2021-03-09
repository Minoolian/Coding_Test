# 직사각형의 길이 찾기

# 조건문을 이용한 간단한 풀이
# https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=3&problemLevel=4&problemLevel=5&contestProbId=AWFPmsqqALwDFAV0&categoryId=AWFPmsqqALwDFAV0&categoryType=CODE&problemTitle=&orderBy=RECOMMEND_COUNT&selectCodeLang=PYTHON&select-1=5&pageSize=30&pageIndex=2

n=int(input())
for tc in range(1, n+1):
    a,b,c=map(int, input().split())

    if a==b: result=c
    elif a==c: result=b
    else: result=a
    print(f"#{tc} {result}")

