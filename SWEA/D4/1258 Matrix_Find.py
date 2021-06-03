# 행렬찾기

# 반복문을 이용한 풀이
# https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=3&problemLevel=4&problemLevel=5&contestProbId=AV18LoAqItcCFAZN&categoryId=AV18LoAqItcCFAZN&categoryType=CODE&problemTitle=&orderBy=RECOMMEND_COUNT&selectCodeLang=PYTHON&select-1=5&pageSize=30&pageIndex=2

t=int(input())
for tc in range(1, t+1):
    n=int(input())
    result={}
    for i in range(n):
        row=list(map(int,input().split()))

        temp=0
        for j in range(n):
            if row[j]:
                temp+=1
            if (not row[j] or j==n-1) and temp :
                result[temp]= result[temp]+1 if temp in result.keys() else 1
                temp=0

    fin=[]
    for col, row in result.items():
        fin.append([row, col, row*col])
    fin.sort(key=lambda x:(x[2],x[0]))

    print(f"#{tc} {len(fin)} {' '.join(list(map(lambda x: ' '.join([str(x[0]),str(x[1])]), fin)))}")

