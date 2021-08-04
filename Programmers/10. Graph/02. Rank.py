# 순위

# 
# https://programmers.co.kr/learn/courses/30/lessons/49191

def solution(n, results):
    answer=0
    adj=[[0 for _ in range(n+1)] for _ in range(n+1)]

    for w,l in results:
        adj[w][l]=2
        adj[l][w]=1

    # for i in range(n+1):
    #     for j in range(n+1):
    #         if adj[i][j]==1:
    #             for k in range(n+1):
    #                 if adj[i][k]==2:
    #                     adj[j][k]=2
    #         elif adj[i][j]==2:
    #             for k in range(n+1):
    #                 if adj[i][k]==1:
    #                     adj[j][k]=1

    for i in range(n+1):
        for j in range(n+1):
            for k in range(n+1):
                if adj[i][j]==1 and adj[i][k]==2:
                    adj[j][k]=2

                elif adj[i][j]==2 and adj[i][k]==1:
                    adj[j][k]=1

    for lis in adj:
        if lis.count(0)==2:
            answer+=1

    return answer

solution(5,[[4, 3], [4, 2], [3, 2], [1, 2], [2, 5]])

