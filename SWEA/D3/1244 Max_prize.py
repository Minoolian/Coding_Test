# 최대 상금

#

def dfs(pos, num, swap):
    if swap==0:
        return num

    if pos==len(num)-2 and swap//2==0:
        return num
    elif pos==len(num)-2 and swap//2==1:
        num[pos], num[pos+1]=num[pos+1], num[pos]
        return num

    m=0
    result=0

    for i in range(pos+1, len(num)):
        if num[i]>num[pos] and num[i]>=m:
            m=num[i]
            clone_num=num[:]
            clone_num[pos], clone_num[i]=clone_num[i], clone_num[pos]
            new_num=dfs(pos+1,clone_num,swap-1)
            if pos==len(num)-3:
                result=int(''.join(map(str,new_num)))
            elif int(''.join(map(str,new_num)))>result:
                result=int(''.join(map(str,new_num)))
    if result!=0:
        return list(map(int,str(result)))
    else:
        return num

t=int(input())

for tc in range(1,t+1):
    temp, swap=map(int,input().split())
    num=list(map(int,str(temp)))

    print("#%d"%tc,''.join(map(str,dfs(0, num, swap))))

