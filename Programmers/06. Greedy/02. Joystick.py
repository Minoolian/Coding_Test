# 조이스틱

#
# https://programmers.co.kr/learn/courses/30/lessons/42860

def solution(name):
    m = [ min(ord(c) - 65, 91-ord(c)) for c in name]

    answer = 0
    where = 0

    while True:
        answer += m[where]
        m[where] = 0

        if sum(m) == 0:
            break

        left, right = (1,1)

        while m[where - left] <= 0:
            left += 1
        while m[where + right] <= 0:
            right += 1

        answer += left if left < right else right
        where += -left if left < right else right

    return answer

solution("JEROEN")

# def solution(name):
#     answer=0
#     check=True
#     for i in range(len(name)):
#         a=ord(name[i])-ord('A')
#         b=ord('Z')-ord(name[i])+1
#         answer+=(b if a>=b else a)
#         if check and name[i]=='A':
#             continue
#         else:
#             if i!=0:
#                 check=False
#             if i!=len(name)-1:
#                 answer+=1
#
#     return answer


