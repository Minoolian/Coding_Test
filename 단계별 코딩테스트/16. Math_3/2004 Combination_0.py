# 조합 0의 갯수

#nCm의 끝자리 0의 갯수를 구하라

def check(k,n):
    count=0
    while(k!=0):
        k=k//n
        count+=k
    return count

n,m=map(int,input().split())

five=check(n,5)-check(m,5)-check(n-m,5)
two=check(n,2)-check(m,2)-check(n-m,2)
# nCm 에 존재하는 2와 5의 갯수 중 최솟값(10의 갯수)

print(min(five,two))



# 시간초과 코드
# from math import factorial
#
# n,m=map(int,input().split())
# k=factorial(n)//(factorial(m)*factorial(n-m))
# result=0
#
# while k%10==0:
#     k=k//10
#     result+=1
#
# print(result)