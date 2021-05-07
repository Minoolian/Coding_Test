from collections import Counter
import sys

sys.setrecursionlimit(10**6)

def search(l,r,g,gems,q,flag,result_len,result):

    if l>=len(gems) or r>=len(gems):
        return result

    if flag:
        if g[gems[r]]==0:
            q+=1
        g[gems[r]]+=1

    if q==len(g.keys()):
        if result_len>r-l+1:
            result_len=r-l+1
            result=[l+1,r+1]

        g[gems[l]]-=1
        if g[gems[l]]==0:
            q-=1
        result=search(l+1,r,g,gems,q,0,result_len,result)
    else:
        result=search(l,r+1,g,gems,q,1,result_len,result)

    return result


def solution(gems):
    g=Counter(gems)

    for key in g.keys(): g[key]=0
    result=search(0,0,g,gems,0,1,float('inf'),[])

    return result



print(solution(["DIA", "RUBY", "RUBY", "DIA", "DIA", "EMERALD", "SAPPHIRE", "DIA"]))
