# 원재의 메모리 복구하기

# 간단한 List를 활용한 풀이
# https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV19AcoKI9sCFAZN&categoryId=AV19AcoKI9sCFAZN&categoryType=CODE

t=int(input())

for tc in range(1,t+1):
    bin=input()

    check='0'
    count=0
    for i in bin:
        if check!=i:
            count+=1
            check=i

    print("#{} {}".format(tc,count))
