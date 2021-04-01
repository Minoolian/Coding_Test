# 계산기1

# 단순풀이
# https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=3&problemLevel=4&problemLevel=5&contestProbId=AV14mbSaAEwCFAYD&categoryId=AV14mbSaAEwCFAYD&categoryType=CODE&problemTitle=&orderBy=RECOMMEND_COUNT&selectCodeLang=PYTHON&select-1=5&pageSize=30&pageIndex=2

for tc in range(1, 11):
    l=int(input())
    form=input()

    result=0
    for i in form:
        if i!='+':
            result+=int(i)
    print("#{} {}".format(tc, result))