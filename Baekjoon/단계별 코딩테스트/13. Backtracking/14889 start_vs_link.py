# N_M_2 예제에서 응용하여 사람_0 과 팀을 이루는 모든 경우의 수를 찾고, 이외의 인원은 상대 팀임을 이용
import sys

n=int(sys.stdin.readline().rstrip())
arr=[list(map(int,sys.stdin.readline().split())) for _ in range(n)]
check=[False]*n #유망한 노드인지 확인
result=[0]*(n//2)
min_num=sys.maxsize

def dfs(index):
    global min_num

    if index==n//2: # DFS의 깊이(횟수)가 같으면 결과를 리턴
        start=0
        link=0
        # result = start 팀의 인원 , vs = link 팀의 인원
        for i in result:
            for j in result:
                start+=arr[i][j]
        vs=list(set([i for i in range(n)])-set(result)) # 차집합을 이용하기 위한 set
        for i in vs:
            for j in vs:
                link+=arr[i][j]
        min_num=min(min_num,abs(start-link))
        return

    for i in range(n):
        if check[i]: # 유망한 노드가 아니면 (True가 유망하지 않은 노드)
            continue
        check[i]=True
        result[index]=i

        if result[0] != 0: # 1부터는 출력하지 않기위한 임시방편
            print(min_num)
            exit(0)

        dfs(index+1)

        for j in range(i+1,n):# 이전 문제와 달리 상위 노드에서 뒷 부분만을 유망한 노드로 설정 (이전 노드들이 다시 나타나면 중복되기에)
            check[j]=False

dfs(0)


# itertools 모듈의 combinations 를 이용한 풀이 / https://hwiyong.tistory.com/307
# 재귀의 방법을 사용하지 않았다.
# from itertools import combinations
#
# N = int(input())
# ability_board = []
# for _ in range(N):
#     ability_board.append(list(map(int, input().split())))
#
# num_list = [i for i in range(N)]
# res = float('inf') # 무한대
#
#
# def solve():
#     global res
#
#     # 조합을 이용하여 각 후보자를 생성함
#     for cand in combinations(num_list, N // 2):
#         # 선택된 후보와 나머지
#         start_member = list(cand)
#         link_member = list(set(num_list) - set(cand))
#
#         # 점수 비교는 2명씩 이루어진다.
#         start_comb = list(combinations(start_member, 2))
#         link_comb = list(combinations(link_member, 2))
#
#         # 점수 구하기
#         start_sum = 0
#         for x, y in start_comb:
#             start_sum += (ability_board[x][y] + ability_board[y][x])
#
#         link_sum = 0
#         for x, y in link_comb:
#             link_sum += (ability_board[x][y] + ability_board[y][x])
#
#         # 차이를 구하는 것이므로 abs 사용
#         if (res > abs(start_sum - link_sum)):
#             res = abs(start_sum - link_sum)
#
#
# solve()
# print(res)