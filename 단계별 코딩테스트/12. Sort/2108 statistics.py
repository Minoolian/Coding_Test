import sys
from collections import Counter # 원소의 갯수를 딕셔너리 형식으로 반환

def ave(lis):
    return sum(lis)/len(lis)

def mid(lis):
    if len(lis)%2!=0:
        return lis[len(lis)//2]
    else:
        return (lis[len(lis)//2]+lis[len(lis)//2-1])/2
def fre(lis):
    cnt=Counter(lis)
    cnt=sorted(cnt.items(),key=lambda x: x[1],reverse=True)
    #sort의 key(정렬기준)를 설정할 때 lambda식 사용이 가능하다
    if cnt[0][1] == cnt[1][1]:
        return cnt[1][0]
    else:
        return cnt[0][0]

def ran(lis):
    return lis[len(lis)-1]-lis[0]

N=int(input())

lis=[int(sys.stdin.readline().rstrip()) for i in range(N)]

lis=sorted(lis)

print(round(ave(lis)))
if N==1:
    print(lis[0])
    print(lis[0])
    print(0)
    exit(0)

print(mid(lis))
print(fre(lis))
print(ran(lis))