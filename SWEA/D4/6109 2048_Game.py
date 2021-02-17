# 추억의 2048 게임

# 리스트를 이용한 풀이.
# https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=3&problemLevel=4&problemLevel=5&contestProbId=AWbrg9uabZsDFAWQ&categoryId=AWbrg9uabZsDFAWQ&categoryType=CODE&problemTitle=&orderBy=RECOMMEND_COUNT&selectCodeLang=PYTHON&select-1=5&pageSize=30&pageIndex=2

def play(s):

    if s=="up":
        for k in range(n):
            idx=0
            tmp=0
            for i in range(n):
                if t[i][k]==0:
                    # 0을 만나면
                    continue
                if tmp==0:
                    # 0이 아닌데 임시값도 저장이 안된경우
                    tmp=t[i][k]
                    continue
                else:
                    # 0이 아닌데 임시값이 저장된 경우
                    if tmp==t[i][k]:
                        # 임시값과 같으면 합치고 idx로 집어넣는다.
                        t[idx][k]=tmp*2
                        idx+=1
                        tmp=0
                    else:
                        # 임시값과 같지 않으면 합치지않고 지나간다.
                        t[idx][k]=tmp
                        tmp=t[i][k]
                        idx+=1

            if tmp:
                t[idx][k]=tmp
                idx+=1


            for j in range(idx,n):
                t[j][k]=0

    elif s=="down":
        for k in range(n):
            idx=n-1
            tmp=0
            for i in range(n-1, -1, -1):
                if t[i][k]==0:
                    # 0을 만나면
                    continue
                if tmp==0:
                    # 0이 아닌데 임시값도 저장이 안된경우
                    tmp=t[i][k]
                    continue
                else:
                    # 0이 아닌데 임시값이 저장된 경우
                    if tmp==t[i][k]:
                        # 임시값과 같으면 합치고 idx로 집어넣는다.
                        t[idx][k]=tmp*2
                        idx-=1
                        tmp=0
                    else:
                        # 임시값과 같지 않으면 합치지않고 지나간다.
                        t[idx][k]=tmp
                        tmp=t[i][k]
                        idx-=1

            if tmp:
                t[idx][k]=tmp
                idx-=1


            for j in range(0,idx+1):
                t[j][k]=0


    elif s=="left":

        for k in range(n):
            idx=0
            tmp=0
            for i in range(n):
                if t[k][i]==0:
                    # 0을 만나면
                    continue
                if tmp==0:
                    # 0이 아닌데 임시값도 저장이 안된경우
                    tmp=t[k][i]
                    continue
                else:
                    # 0이 아닌데 임시값이 저장된 경우
                    if tmp==t[k][i]:
                        # 임시값과 같으면 합치고 idx로 집어넣는다.
                        t[k][idx]=tmp*2
                        idx+=1
                        tmp=0
                    else:
                        # 임시값과 같지 않으면 합치지않고 지나간다.
                        t[k][idx]=tmp
                        tmp=t[k][i]
                        idx+=1

            if tmp:
                t[k][idx]=tmp
                idx+=1


            for j in range(idx,n):
                t[k][j]=0

    elif s=="right":

        for k in range(n):
            idx=n-1
            tmp=0
            for i in range(n-1,-1,-1):
                if t[k][i]==0:
                    # 0을 만나면
                    continue
                if tmp==0:
                    # 0이 아닌데 임시값도 저장이 안된경우
                    tmp=t[k][i]
                    continue
                else:
                    # 0이 아닌데 임시값이 저장된 경우
                    if tmp==t[k][i]:
                        # 임시값과 같으면 합치고 idx로 집어넣는다.
                        t[k][idx]=tmp*2
                        idx-=1
                        tmp=0
                    else:
                        # 임시값과 같지 않으면 합치지않고 지나간다.
                        t[k][idx]=tmp
                        tmp=t[k][i]
                        idx-=1

            if tmp:
                t[k][idx]=tmp
                idx-=1


            for j in range(0,idx+1):
                t[k][j]=0


if __name__ == "__main__":

    t=int(input())
    for tc in range(1, t+1):
        n, s=input().split()
        n=int(n)
        #t=list(map(int,input().split()))
        t=[list(map(int,input().split())) for _ in range(int(n))]

        play(s)
        print(f"#{tc}")
        for p in t:
            print(*p)


