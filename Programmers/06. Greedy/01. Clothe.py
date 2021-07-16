# 체육복

# 그리디한 풀이 방법 (Set 집합을 사용해도 간결하다)
# https://programmers.co.kr/learn/courses/30/lessons/42862

def solution(n, lost, reserve):
    for i in range(1,n+1):
        if (i in lost) and (i in reserve):
            lost.remove(i)
            reserve.remove(i)

    student=[0]+[2 if i in reserve else 1 for i in range(1,n+1)]+[0]

    for idx in lost:
        student[idx]-=1
        if student[idx-1]==2:
            student[idx]+=1
            student[idx-1]-=1
        if student[idx+1]==2:
            student[idx]+=1
            student[idx+1]-=1

    return student.count(1)+student.count(2)