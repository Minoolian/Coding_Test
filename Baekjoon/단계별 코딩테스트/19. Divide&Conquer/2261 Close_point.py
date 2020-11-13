# 가장 가까운 두 점

# 각각의 좌표는 절댓값이 10,000을 넘지 않는 정수이다. 같은 점이 여러 번 주어질 수도 있다.
# 가장 가까운 두 점의 거리의 제곱 출력

import sys

def distance(a,b):
    return (a[0]-b[0])**2+(a[1]-b[1])**2

def solve(start, end):
    leng = end-start
    if leng ==2:
        return distance(lis[start],lis[start+1])
    elif leng ==3:
        return min(distance(lis[start],lis[start+1]), distance(lis[start],lis[start+2]), distance(lis[start+1],lis[start+2]))
    
    leng = (start+end)//2
    mid = lis[leng][0] # 가운데 점의 x좌표
    d= min(solve(start,leng),solve(leng,end))

    temp=[]
    for i in range(start,end): # 중앙을 기준으로 양쪽 두 점 중 최단거리가 있는 지 검사
        if (mid-lis[i][0])**2 < d:
            temp.append(lis[i])
    temp.sort(key=lambda x:x[1]) # y좌표를 기준으로 정렬
    m=d
    temp_leng=len(temp)

    if temp_leng>=2: # 1개이면 한개의 점만 찾은 것이므로 수행할 필요가 없다. (가로지르는 값중 최소값은 없다)
        for i in range(temp_leng-1):
            for j in range(i+1,temp_leng): # 모든 쌍을 검사
                if (temp[i][1] - temp[j][1])**2 > d: # 오름차순 정렬을 했으므로 이후의 값은 모두 d보다 클 것으므로 break
                    break
                elif temp[i][0] < mid and temp[j][0] < mid: # 가운데를 기준으로 같은 방향에 있는 것은 고려할 필요가 없으므로 생략
                    continue
                elif temp[i][0] > mid and temp[j][0] > mid:
                    continue
                m=min(m, distance(temp[i],temp[j]))
    return m

n=int(sys.stdin.readline())
lis=[list(map(int,sys.stdin.readline().split())) for _ in range(n)]
lis=list(set(map(tuple,lis)))
# 중복을 제거하는 방법: set(2차원 list)는 중복이 제거되지 않는다.
# tuple을 이용해야 하는 것 같다.

if n!=len(lis): # 중복좌표가 있다는 것은 최단 거리가 0이다.
    print("0")
else:
    lis.sort() # x좌표를 기준으로 정렬
    print(solve(0,len(lis)))