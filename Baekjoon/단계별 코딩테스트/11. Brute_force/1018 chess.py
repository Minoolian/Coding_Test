# 입력받은 체스 판을 매 8*8 판으로 잘라서 B 체스판과 W 체스판을 각각 비교한 후 최소값 출력

M,N=map(int,input().split())
chess=[]
for _ in range(M):
    chess.append(input())

W_chess=[[None for _ in range(8)] for _ in range(8)]
B_chess=[[None for _ in range(8)] for _ in range(8)]
p_1='W'
for i in range(8):
    p_2=p_1
    for j in range(8):
        W_chess[i][j]=p_2
        if p_2 == 'B':
            p_2 = 'W'
        elif p_2 == 'W':
            p_2 = 'B'
    if p_1 == 'B':
        p_1='W'
    elif p_1 == 'W':
        p_1='B'

p_1='B'
for i in range(8):
    p_2=p_1
    for j in range(8):
        B_chess[i][j]=p_2
        if p_2 == 'B':
            p_2 = 'W'
        elif p_2 == 'W':
            p_2 = 'B'
    if p_1 == 'B':
        p_1='W'
    elif p_1 == 'W':
        p_1='B'


change=[]
for m in range(M-7):
    for n in range(N-7):
        count=0
        for i in range(8):
            for j in range(8):
                if chess[m+i][n+j]!=W_chess[i][j]:
                    count+=1
        change.append(count)
        count = 0
        for i in range(8):
            for j in range(8):
                if chess[m + i][n + j] != B_chess[i][j]:
                    count += 1
        change.append(count)

print(min(change))