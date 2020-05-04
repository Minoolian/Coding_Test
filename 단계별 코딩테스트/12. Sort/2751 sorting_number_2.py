# 합병정렬(병합정렬)을 이용한 방법 (pypy3 로 실행해야 통과한다)
import sys

N=int(input())
number=[]
for _ in range(N):
    number.append(int(sys.stdin.readline().rstrip()))

def merge(left,right):
    i=0 ; j=0
    sorted_list=[]

    while(i<len(left)) and (j<len(right)):
        if left[i] < right[j]:
            sorted_list.append(left[i])
            i+=1
        else:
            sorted_list.append(right[j])
            j+=1

    while i<len(left):
        sorted_list.append(left[i])
        i+=1

    while j<len(right):
        sorted_list.append(right[j])
        j+=1

    return sorted_list

def merge_sort(unsorted_list):

    if len(unsorted_list)<=1:
        return unsorted_list

    mid=len(unsorted_list)//2
    left=unsorted_list[:mid]
    right=unsorted_list[mid:]

    left1=merge_sort(left)
    right1=merge_sort(right)
    return merge(left1,right1)

for i in merge_sort(number):
    print(i)


# 파이썬 내장함수를 이용한 간단한 방법
# import sys
# N = int(sys.stdin.readline())
# arr = [int(sys.stdin.readline()) for _ in range(N)]
# sys.stdout.write("\n".join(map(str, sorted(arr))))
