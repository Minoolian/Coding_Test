# 버블 소트

# 첫째 줄에 N
# 다음 줄에는 N개의 정수로 A[1], A[2], …, A[N]이 주어진다.
#
# Swap 횟수를 출력한다

import sys
input=sys.stdin.readline

def query(idx):
    ret=0
    while idx:
        ret+=fenwick[idx]
        idx-=idx&-idx

    return ret

def update(idx, val):
    while idx<=n:
        fenwick[idx]+=val
        idx+=idx&-idx

if __name__=="__main__":
    n=int(input())
    arr=[]
    temp=list(map(int,input().split()))

    j=0
    for i in temp:
        arr.append([i,j])
        j+=1
    arr.sort(reverse=True)

    fenwick=[0 for _ in range(n+1)]

    ans=0
    for a,b in arr:
        b+=1
        ans+=query(b-1)
        update(b,1)

    print(ans)