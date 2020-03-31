# https://claude-u.tistory.com/39 참고 수정코드
student_score=[]
for i in range(5):
    score=int(input())
    if score<40:
        student_score.append(40)
    else:
        student_score.append(score)

print(int(sum(student_score)/len(student_score)))

# 내가 작성한 코드
# student_score=[]
# for i in range(5):
#     student_score.append(int(input()))
# sum=0
#
# for i in student_score:
#     if i<40:
#         i=40
#     sum+=i
#
# print(int(sum/len(student_score)))
