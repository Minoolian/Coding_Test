# 가장 큰 수

# str의 사전식 정렬을 이용한 풀이
# https://programmers.co.kr/learn/courses/30/lessons/42746

def solution(numbers):

    return str(int(''.join(sorted(map(str,numbers),key=lambda x:x*3,reverse=True))))


print(solution([90,908,89,898,10,101,1,8,9]))



# 2. 병합정렬 (시간초과)
# def merge(left, right):
#     i,j=0,0
#     sorted_list=[]
#
#     while i<len(left) and j<len(right):
#         l,r=str(left[i]), str(right[j])
#         for k in range(max(len(l),len(r))):
#             if min(len(l),len(r))<=k:
#                 if l[-1]>r[-1]:
#                     sorted_list.append(l)
#                     i+=1
#                 else:
#                     sorted_list.append(r)
#                     j+=1
#                 break
#
#             if l[k]>r[k]:
#                 sorted_list.append(l)
#                 i+=1
#                 break
#
#             elif l[k]<r[k]:
#                 sorted_list.append(r)
#                 j+=1
#                 break
#
#     while i<len(left):
#         sorted_list.append(str(left[i]))
#         i+=1
#
#     while j<len(right):
#         sorted_list.append(str(right[j]))
#         j+=1
#
#     return sorted_list
#
#
# def sort(numbers):
#
#     if len(numbers)<=1:
#         return numbers
#
#     mid=len(numbers)//2
#     left=numbers[:mid]
#     right=numbers[mid:]
#
#     left1=sort(left)
#     right1=sort(right)
#
#     return merge(left1,right1)
#
#
# def solution(numbers):
#
#     return ''.join(sort(numbers))
#
# print(solution([212,21]))


# 1. 같은 수가 있을때 구별이 불가
# def solution(numbers):
#
#     return int(''.join(map(numbers,sorted(a,key=lambda x:(str(x)[0],str(x)[1] if len(str(x))>1 else str(x)[0],str(x)[2] if len(str(x))>2 else str(x)[0],str(x)[3] if len(str(x))>3 else str(x)[0]),reverse=True))))
