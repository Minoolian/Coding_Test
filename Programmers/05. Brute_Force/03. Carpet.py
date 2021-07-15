# 카펫

#
# https://programmers.co.kr/learn/courses/30/lessons/42842

def solution(brown, yellow):
    row=3
    for col in range(brown//2-1,2,-1):
        if (col*row)-brown == yellow:
            return [col,row]
        else:
            row+=1