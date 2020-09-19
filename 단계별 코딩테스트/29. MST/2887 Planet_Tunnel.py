# 행성 터널

# 터널을 총 N-1개 건설해서 모든 행성이 서로 연결되게 하려고 한다. 이때, 모든 행성을 터널로 연결하는데 필요한 최소 비용을 구하는 프로그램

# 첫째 줄에 행성의 개수 N
# 다음 N개 줄에는 각 행성의 x, y, z좌표가 주어진다.

import sys
#크루스칼에 필요한 유니온 파인드
def Find(x):
    if p[x]==x:
        return x
    else:
        y=Find(p[x])
        p[x]=y
        return y

def Union(x,y):
    x=Find(x)
    y=Find(y)
    if x!=y:
        p[y]=x

N=int(sys.stdin.readline())
s_location=[]
p=[i for i in range(N)]
e=[]
for i in range(N):
    x,y,z=map(int,sys.stdin.readline().split())
    s_location.append([x,y,z,i])#x,y,z좌표 i번째노드

for j in range(3):
    s_location.sort(key=lambda x:x[j])#각 좌표별로 정렬
    before_location=s_location[0][3]
    for i in range(1,N):#각 좌표별로 간선추가
        cur_location=s_location[i][3]
        e.append([abs(s_location[i][j]-s_location[i-1][j]),before_location,cur_location])
        before_location=cur_location


e.sort(key=lambda x:x[0])

#크루스칼 알고리즘
count=0
result=0
for dis,start,end in e:
    if Find(start)!=Find(end):
        result+=dis

        Union(start,end)
    if count==N-1:
        break

print(result)