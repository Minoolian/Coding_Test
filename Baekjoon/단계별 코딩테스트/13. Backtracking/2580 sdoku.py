import sys

arr=[list(map(int,input().split())) for _ in range(9)] # 입력받은 스도쿠 판
zero=[(i,j) for i in range(9) for j in range(9) if arr[i][j]==0] # 0이 있는 좌표를 저장
candidate=[0 for _ in range(len(zero))] # 1~9 까지 가능한 후보군 리스트

def dfs(index):
    if index==len(zero): # 9가 되면 판을 출력 (0~8)
        for i in arr:
            print(*i) # 리스트의 [] 없이 출력하는 방법
        sys.exit(0) # 여러가지 경우이면 하나만 출력

    x=zero[index][0] # 스도쿠판의 0인 값의 x좌표
    y=zero[index][1] # 스도쿠판의 0인 값의 y좌표

    candidate[index]=isPromising(x, y) # 각 시도의 후보값 리스트
    if candidate[index].count(True)!=0:
        for i in [i for i,k in enumerate(candidate[index]) if k]: # enumerate: (인덱스, 값)을 반환한다.
            arr[x][y]=i
            dfs(index+1)
            arr[x][y]=0 # 해당 노드들의 DFS에 영향을 주지 않기 위해 설정


def isPromising(x,y):
    possible=[False]+[True for _ in range(9)]

    for i in range(9):
        possible[arr[i][y]]=False # 열에 존재하는 값을 유망하지 않은 것으로 설정
        possible[arr[x][i]]=False # 행에 존재하는 값을 유망하지 않은 것으로 설정

    for i in range(3):
        for j in range(3):
            possible[arr[x//3*3+i][y//3*3+j]]=False # 3*3 안에 존재하는 값을 유망하지 않은 것으로 설정

    return possible # 최종적으로 유망한 값을 반환

dfs(0)