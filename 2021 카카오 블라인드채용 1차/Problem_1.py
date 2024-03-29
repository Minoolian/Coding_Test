
def solution(new_id):

    result_1=[]
    for prac in new_id:
        if prac>='A' and prac<='Z':
            result_1.append(prac.lower())
        if (prac>='a' and prac<='z') or (prac>='0' and prac<='9') or prac=='.' or prac=='_' or prac=='-':
            result_1.append(prac)

    result_3=[]
    flag=False
    for prac in result_1:
        if prac=='.':
            if flag:
                continue
            flag=True
        else:
            flag=False

        result_3.append(prac)

    result_4=[]
    for i in range(len(result_3)):
        if result_3[i]=='.' and (i==0 or i==len(result_3)-1):
            continue
        result_4.append(result_3[i])

    if len(result_4)==0:
        result_4=['a']

    result_6=result_4
    if len(result_4)>=16:
        if result_4[14]=='.':
            result_6=result_4[:14]
        else:
            result_6=result_4[:15]

    if len(result_6)<=2:
        while len(result_6)<3:
            result_6.append(result_6[-1])

    return ''.join(result_6)


while True:
    a=input()
    print(solution(a))


# 다른 사람 풀이
# import re
#
# def solution(new_id):
#     st = new_id
#       ...!@BaT#*..y.abcdefghijklm
#     st = st.lower()
#       ...!@bat#*..y.abcdefghijklm
#     st = re.sub('[^a-z0-9\-_.]', '', st)
#       ...bat..y.abcdefghijklm
#     st = re.sub('\.+', '.', st)
#       .bat.y.abcdefghijklm
#     st = re.sub('^[.]|[.]$', '', st)
#       bat.y.abcdefghijklm
#     st = 'a' if len(st) == 0 else st[:15]
#       bat.y.abcdefghi
#     st = re.sub('^[.]|[.]$', '', st)
#       bat.y.abcdefghi
#     st = st if len(st) > 2 else st + "".join([st[-1] for i in range(3-len(st))])
#       bat.y.abcdefghi
#     return st