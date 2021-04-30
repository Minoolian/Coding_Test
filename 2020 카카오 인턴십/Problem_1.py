def calc(x,y):
    if x=='*': x=10
    if x=='#': x=11
    dial=[[3,1],[0,0],[0,1],[0,2],[1,0],[1,1],[1,2],[2,0],[2,1],[2,2],[3,0],[3,2]]

    return abs(dial[x][0]-dial[y][0]) + abs(dial[x][1]-dial[y][1])


def trans(numbers, hand):

    result=''
    left='*'; right='#'

    for i in numbers:
        if i in [1,4,7]:
            left=i; result+="L"
        elif i in [3,6,9]:
            right=i; result+="R"
        else:
            if calc(left,i)>calc(right,i):
                right=i; result+="R"
            elif calc(left,i)<calc(right,i):
                left=i; result+="L"
            else:
                if hand=="left":
                    left=i; result+="L"
                elif hand=="right":
                    right=i; result+="R"

    return result


def solution(numbers, hand):
    answer = trans(numbers, hand)
    return answer