# 햄버거 다이어트

# 부분집합을 이용한 풀이 (powerset : 모든부분집합으로 구성된 즉 멱집합)
# https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AWT-lPB6dHUDFAVT&categoryId=AWT-lPB6dHUDFAVT&categoryType=CODE

def powerset(idx, s,c):
    global ms

    if c>l : return
    if c<=l : ms=max(ms,s)
    if idx==n : return

    powerset(idx+1, s+tk[idx][0], c+tk[idx][1])
    powerset(idx+1, s, c)

t=int(input())

for tc in range(1, t+1):

    n, l=map(int,input().split())
    tk=[list(map(int,input().split())) for _ in range(n)]
    ms=0

    powerset(0, 0, 0)
    print(f"#{tc} {ms}")