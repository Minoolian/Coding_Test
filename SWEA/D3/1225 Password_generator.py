# 암호생성기

# list를 이용한 풀이.
# https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV14uWl6AF0CFAYD&categoryId=AV14uWl6AF0CFAYD&categoryType=CODE

from collections import deque

for tc in range(1,11):
    input()
    password=deque(map(int,input().split()))

    var=1
    while True:
        num=password.popleft()
        if num-var<=0:
            password.append(0)
            break

        password.append(num-var)

        if var==5:
            var=1
        else:
            var+=1

    print("#{} {}".format(tc," ".join(map(str,password))))

