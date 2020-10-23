# 최대 상금

# DFS를 이용하여 가능한 경우의 수를 찾는 문제 (백트래킹)
# https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV15Khn6AN0CFAYD

def dfs(pos, num, swap):
    global result
    if swap==0:
        result=max(result,int(''.join(map(str,num))))
        return

    if pos==len(num)-2 and swap%2==0:
        swap=0
        dfs(pos,num,swap)

    elif pos==len(num)-2 and swap%2==1:
        num[pos], num[pos+1]=num[pos+1], num[pos]
        swap=0
        dfs(pos,num,swap)

    else:
        m=0
        flag=1
        for i in range(pos, len(num)):
            for j in range(i+1,len(num)):
                if num[j]>=num[i]:
                    m=num[i]
                    clone_num=num[:]
                    clone_num[j], clone_num[i]=clone_num[i], clone_num[j]
                    dfs(i,clone_num,swap-1)
                    flag=0
        if flag:
            dfs(pos+1, num, swap)


t=int(input())

for tc in range(1,t+1):
    temp, swap=map(int,input().split())
    num=list(map(int,str(temp)))
    result=0

    dfs(0, num, swap)
    print("#{} {}".format(tc, result))

