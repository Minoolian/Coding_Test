# 준환이의 양팔저울

# DFS와 비트마스크를 이용한 풀이
# https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AWAe7XSKfUUDFAUw&categoryId=AWAe7XSKfUUDFAUw&categoryType=CODE
exp = [ 1, 2, 4, 8, 16, 32, 64, 128, 256, 512 ]
fact = [ 0, 1, 2, 6, 24, 120, 720, 5040, 40320, 362880 ]

def dfs(check, cnt, left, right):
    global result

    if cnt==n:
        result+=1
        return

    if left>=(s-left):
        result+=exp[n-cnt]*fact[n-cnt]
        return

    for i in range(n):
        if check & (1<<i) ==0:
            dfs(check|(1<<i), cnt+1, left+value[i], right)
            if left>=right+value[i]:
                dfs(check|(1<<i), cnt+1, left, right+value[i])

t=int(input())

for tc in range(1, t+1):
    n=int(input())
    value=list(map(int,input().split()))
    s=sum(value)
    result=0

    dfs(0, 0, 0, 0)
    print("#{} {}".format(tc,result))

# 비트마스크와 DP를 이용한 풀이 (SWEA 참고)
# def DFS(cnt, l, r):
#     global N, G, visit, check
#     result = 0
#
#     if l < r:
#         return 0
#
#     if check[visit][l] != 0:
#         return check[visit][l]
#
#     if cnt == N:
#         return 1
#
#     for i in range(N):
#         if visit & (1 << i) == 0:
#             visit = visit | (1 << i)
#             result += DFS(cnt+1, l + G[i], r)
#             result += DFS(cnt+1, l, r + G[i])
#             visit = visit ^ (1 << i)
#
#     check[visit][l] = result
#
#     # for i, v in enumerate(visit):
#     #     if v == 0:
#     #         visit[i] = 1
#     #         result += DFS(l+G[i], r)
#     #         result += DFS(l, r+G[i])
#     #         visit[i] = 0
#
#     return result
#
#
#
#
# T = int(input())
# for test_case in range(1, T + 1):
#     N = int(input())
#     G = list(map(int, str(input()).split()))
#     visit = 0
#
#     G_sum = sum(G) + 1
#     visit_num_ = 2**N
#     check = [[0 for _ in range(G_sum)] for _ in range(visit_num_)]    # ( visit, l, r )
#
#
#     count = DFS(0, 0, 0)
#
#     print(f'#{test_case} {count}')