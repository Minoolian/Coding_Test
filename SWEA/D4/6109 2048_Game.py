# 추억의 2048 게임

#
# https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=3&problemLevel=4&problemLevel=5&contestProbId=AWbrg9uabZsDFAWQ&categoryId=AWbrg9uabZsDFAWQ&categoryType=CODE&problemTitle=&orderBy=RECOMMEND_COUNT&selectCodeLang=PYTHON&select-1=5&pageSize=30&pageIndex=2

def play(s):
    if s=="up":
        r=range(n)
    elif s=="down"
        r=range(n-1,-1,-1)



    for k in range(n):
        idx=0
        tmp=0
        for i in range(n):
            if t[i]==0:
                # 0을 만나면
                continue
            if tmp==0:
                # 0이 아닌데 임시값도 저장이 안된경우
                tmp=t[i]
                continue
            else:
                # 0이 아닌데 임시값이 저장된 경우
                if tmp==t[i]:
                    # 임시값과 같으면 합치고 idx로 집어넣는다.
                    t[idx]=tmp*2
                    idx+=1
                    tmp=0
                else:
                    # 임시값과 같지 않으면 합치지않고 지나간다.
                    t[idx]=tmp
                    tmp=t[i]
                    idx+=1

        if tmp:
            t[idx]=tmp
            idx+=1

        for j in range(idx,n):
            t[j]=0


n, s=input().split()
n=int(n)
#t=list(map(int,input().split()))
t=[list(map(int,input().split())) for _ in range(int(n))]

play(s)
print(t)


