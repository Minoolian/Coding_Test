# 준환이의 운동관리

# 조건문을 이용한 풀이
# https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AWE_ZXcqAAMDFAV2&categoryId=AWE_ZXcqAAMDFAV2&categoryType=CODE

t=int(input())

for tc in range(1, t+1):
    l,u,x=map(int,input().split())

    if l<=x<=u:
        result=0
    elif x<l:
        result=l-x
    else:
        result=-1

    print(f"#{tc} {result}")