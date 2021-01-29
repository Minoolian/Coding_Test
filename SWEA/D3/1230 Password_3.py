# 암호문3

# 조건문을 이용한 풀이
# https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=3&problemLevel=4&problemLevel=5&contestProbId=AV14zIwqAHwCFAYD&categoryId=AV14zIwqAHwCFAYD&categoryType=CODE&problemTitle=&orderBy=RECOMMEND_COUNT&selectCodeLang=PYTHON&select-1=5&pageSize=30&pageIndex=2

for tc in range(1,11):
    n=int(input())
    pw=list(map(int,input().split()))
    c=int(input())
    cmd=list(map(str,input().split()))

    i=0
    while c:
        op=cmd[i]
        if op=="I":
            for j in range(int(cmd[i+2])):
                pw.insert(int(cmd[i+1])+j,int(cmd[i+3+j]))
            i=i+3+int(cmd[i+2])
        elif op=="D":
            for _ in range(int(cmd[i+2])):
                pw.pop(int(cmd[i+1])-1)
            i=i+3
        elif op=="A":
            for j in range(int(cmd[i+1])):
                pw.append(int(cmd[i+2+j]))
            i=i+2+int(cmd[i+1])
        c-=1

    print("#{} {}".format(tc,' '.join(map(str,pw[:10]))))