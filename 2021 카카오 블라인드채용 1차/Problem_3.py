from bisect import bisect_left

def idx(info_sep):
    ind=[]
    for p in info_sep:
        if p=="cpp": ind.append(0)
        if p=="java": ind.append(1)
        if p=="python": ind.append(2)
        if p=="backend": ind.append(0)
        if p=="frontend": ind.append(1)
        if p=="junior": ind.append(0)
        if p=="senior": ind.append(1)
        if p=="chicken": ind.append(0)
        if p=="pizza": ind.append(1)
        if p=="-": ind.append(-1)
    return ind

def groupfy(info):
    group=[[[[[] for _ in range(2)] for _ in range(2)] for _ in range(2)] for _ in range(3)]
    for info_sep in info:
        info_sep=info_sep.split()
        i,j,k,l=idx(info_sep)
        group[i][j][k][l].append(int(info_sep.pop()))
        group[i][j][k][l].sort()
    return group

def solution(info, query):
    answer = []

    group=groupfy(info)

    for q in query:
        q=q.split(" and ")
        for sep in q.pop().split():
            q.append(sep)

        index=idx(q)
        score=int(q.pop())

        suit=0
        for i in range(3):
            if index[0]!=-1 and i!=index[0]: continue
            for j in range(2):
                if index[1]!=-1 and j!=index[1]: continue
                for k in range(2):
                    if index[2]!=-1 and k!=index[2]: continue
                    for l in range(2):
                        if index[3]!=-1 and l!=index[3]: continue
                        suit+=len(group[i][j][k][l])-bisect_left(group[i][j][k][l],score)

        answer.append(suit)

    return answer


# 효율성 0%
# def solution(info, query):
#     answer = []
#
#     for q in query:
#         q=q.split(" and ")
#         for sep in q.pop().split():
#             q.append(sep)
#
#         suit=0
#         for info_sep in info:
#             info_sep=info_sep.split()
#
#             flag=False
#             for i in range(5):
#                 if i==4:
#                     if int(q[i])<=int(info_sep[i]): flag=True
#                     else: break
#
#                 if q[i]==info_sep[i] or q[i]=='-': continue
#                 else: break
#
#             if flag: suit+=1
#             else: continue
#
#         answer.append(suit)
#
#     return answer

print(solution(["java backend junior pizza 150","python frontend senior chicken 210","python frontend senior chicken 150","cpp backend senior pizza 260","java backend junior chicken 80","python backend senior chicken 50"], ["java and backend and junior and pizza 100","python and frontend and senior and chicken 200","cpp and - and senior and pizza 250","- and backend and senior and - 150","- and - and - and chicken 100","- and - and - and - 150"]))