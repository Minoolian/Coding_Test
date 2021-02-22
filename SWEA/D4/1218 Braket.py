# 괄호 짝짓기

# 리스트와 딕셔너리를 이용한 풀이
# https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=3&problemLevel=4&problemLevel=5&contestProbId=AV14eWb6AAkCFAYD&categoryId=AV14eWb6AAkCFAYD&categoryType=CODE&problemTitle=&orderBy=RECOMMEND_COUNT&selectCodeLang=PYTHON&select-1=5&pageSize=30&pageIndex=2

def judge():
    check = []
    answer=True

    for i in str:
        if i in pair.values():
            check.append(i)

        elif i in pair.keys():
            if len(check)==0: # 리스트의 길이가 0 이면 런타임 오류
                answer=False
                break

            if check[-1]==pair[i]: # 짝이 맞는지 확인
                check.pop()
            else:
                answer=False
                break

    if answer and not check:
        return True
    else:
        return False

if __name__=="__main__":
    pair={'}':'{', ']':'[', '>':'<', ')':'('}

    for tc in range(1,11):
        n=int(input())
        str=input()

        result=1 if judge() else 0
        print(f"#{tc} {result}")