import re

def toDeci(st):
    value=str(st.group())
    rep={'zero':'0', 'one':'1', 'two':'2', 'three':'3', 'four':'4', 'five':'5', 'six':'6', 'seven':'7', 'eight':'8', 'nine':'9'}
    result=''

    check=''
    for s in value:
        check+=s
        if check not in rep.keys():
            continue
        else:
            result+=rep[check]
            check=''

    return result

def solution(s):

    answer=re.sub('[a-z]+',toDeci,s)

    return answer

print(solution("one4seveneight"))