# 모의고사

# 완전탐색을 이용한 풀이
# https://programmers.co.kr/learn/courses/30/lessons/42840

# from itertools import cycle

def solution(answers):
    student=[[1,2,3,4,5],[2,1,2,3,2,4,2,5],[3,3,1,1,2,2,4,4,5,5]]
    answer=[0,0,0]

    for i,num in enumerate(answers):
        for j in range(3):
            if student[j][i%len(student[j])]==num:
                answer[j]+=1

    return [n for n,score in enumerate(answer, start=1) if score==max(answer)]