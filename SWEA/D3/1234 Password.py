# 비밀번호

# List를 활용한 풀이.
# https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV14_DEKAJcCFAYD&categoryId=AV14_DEKAJcCFAYD&categoryType=CODE


for tc in range(1,11):
    n, p=input().split()

    result=[p[0]]
    for i in range(1, len(p)):
        if len(result):
            if result[-1]==p[i]:
                result.pop()
            else:
                result.append(p[i])
        else:
            result.append(p[i])

    print(f"#{tc} {''.join(result)}")