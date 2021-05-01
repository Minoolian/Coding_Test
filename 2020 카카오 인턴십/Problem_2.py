from itertools import permutations
from collections import Counter

def solution(expression):
    answer = 0

    operator=[]
    operand=[]
    opd=''
    for frag in expression:
        if frag in ['+','-','*']:
            operand.append(opd)
            operator.append(frag)
            opd=''
        else: opd+=frag
    operand.append(opd)

    opr_num=Counter(operator)

    for p in permutations(opr_num.keys(),len(opr_num.keys())):
        opr=operator[:]
        opd=operand[:]
        for op in p:
            for _ in range(opr_num[op]):
                idx=opr.index(op)
                ex=opd[idx]+op+opd[idx+1]
                opd.pop(idx+1)
                opr.pop(idx)
                opd[idx]=str(eval(ex))

        answer=max(answer,abs(int(opd[0])))


    return answer

print(solution("100-200*300-500+20"))
