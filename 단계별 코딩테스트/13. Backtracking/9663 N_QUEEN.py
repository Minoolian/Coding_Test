# https://pacific-ocean.tistory.com/338
n = int(input())
s = [0 for i in range(16)]
result = 0

def isTrue(x):
    for i in range(1, x):
        if s[x] == s[i] or abs(s[x] - s[i]) == x - i: # 같은열 or 대각선에 퀸 확인
            return False
    return True # 유망한 노드로 지정

def dfs(cnt):
    global result
    if cnt > n: # 판을 넘어가면 경우의 수 추가
        result += 1
    else:
        for i in range(1, n + 1): # (1,1) (2,1) .... (n,1) 까지 확인
            s[cnt] = i # s[열]=행 : 현재 진행중인 노드 저장
            if isTrue(cnt): # 후 유망한 노드인 지 확인
                dfs(cnt + 1)

dfs(1)
print(result)


# https://thd0011.tistory.com/19
# import sys
#
# N=int(sys.stdin.readline().rstrip())
# ans=0
#
# def dfs(row):
#     global ans # 전역변수를 함수 내로 불러들이기 위한 사용
#     global N
#
#     if row>N:
#         ans+=1
#     else:
#         for i in range(1,N+1):
#             col[row]=i
#
#             if isPossible(row):
#                 dfs(row+1)
#             else:
#                 col[row]=0
#
# def isPossible(c):
#
#     for i in range(1,c):
#         if col[i] == col[c]:
#             return False
#
#         if abs(col[i]-col[c])==abs(i-c):
#             return False
#
#     return True
#
#
# for i in range(1,N+1):
#     col = [0 for _ in range(16)]
#     col[1]=i
#
#     dfs(2)
#
# print(ans)




# https://mygumi.tistory.com/199

