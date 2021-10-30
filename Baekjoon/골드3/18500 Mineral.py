# 미네랄2

# BFS를 이용한 풀이
# https://www.acmicpc.net/problem/18500

dx=[1,-1,0,0]
dy=[0,0,1,-1]

def destroy(h, flag):
    if 'x' not in cave[h-1]:
        return False if flag else True

    if flag:
        for i in range(C):
            if cave[h-1][i]=='x':
                cave[h-1][i]='.'
                break
    else:
        for i in range(C-1, -1, -1):
            if cave[h-1][i]=='x':
                cave[h-1][i]='.'
                break
    mineral.remove((h-1,i))

    return False if flag else True

def find():
    m=set()
    for i in range(C):
        q=[]
        if cave[0][i]=='x' and (0,i) not in m:
            q.append((0,i))

        while q:
            x,y=q.pop(0)
            m.add((x,y))

            for idx in range(4):
                nx=x+dx[idx]
                ny=y+dy[idx]

                if 0<=nx<R and 0<=ny<C and cave[nx][ny]=='x' and (nx,ny) not in m and (nx,ny) not in q:
                    q.append((nx,ny))
    return m

def down(comp):
    result=float('inf')
    for x,y in comp:
        if cave[x-1][y]=='x':
            continue

        depth=0
        check=True
        while 0<=x-1 and cave[x-1][y]=='.':
            depth+=1
            x-=1
            if (x-1,y) in comp:
                check=False
                break
        if check:
            result=min(result, depth)

    # for x,y in comp:
    #     cave[x-result][y]='x'
    # for x,y in comp:
    #     cave[x][y]='.'

    check=[]
    for x,y in comp:
        check.append((x-result,y))
        mineral.add((x-result,y))
        if (x,y) not in check:
            cave[x][y]='.'
            mineral.remove((x,y))
        cave[x-result][y]='x'



R,C=map(int,input().split())
cave=[None for _ in range(R)]
mineral=set()
for i in range(R-1,-1,-1):
    temp=list(input())
    cave[i]=temp
    for j in range(C):
        if temp[j]=='x':
            mineral.add((i,j))

N=int(input())
height=map(int,input().split())

flag=True
for h in height:
    flag=destroy(h, flag)
    comp=mineral-find()

    if not comp:
        continue

    down(comp)

for c in cave[::-1]:
    print(''.join(c))



