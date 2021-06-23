# 1
# import re
#
# def solution(S, C):
#     # write your code in Python 3.6
#     answer=''
#     exist={}
#     C=C.lower()
#
#     for st in re.split(',\s',S):
#         sp=re.split('\s',re.sub('[-]','',st.lower()))
#         check=sp[0]+'.'+sp[-1]+'@'+C+'.com'
#
#         if check not in exist:
#             exist[check]=2
#             answer+=st+' <'+check+'>, '
#         else:
#             answer+=st+' <'+sp[0]+'.'+sp[-1]+str(exist[check])+'@'+C+'.com>, '
#             exist[check]+=1
#
#     return (re.sub(',\s$','',answer))`


# 2
# import re
#
# s="""
# 348543545 23 Sep 2009 system.zip
# 3485423124 23 Feb 2009 sys-tem.zip
# """
#
# def calc(size, m, y):
#     months=['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
#     if int(size)>=240*(2**10) and (int(y)>1990 or ((int(y)==1990) and (months.index(m)>0))):
#         return True
#     return False
#
# def solution(S):
#     answer=0
#     p=re.compile('(\d+)\s\d+\s(\w+)\s(\d+)\s\w+.\w+',re.DOTALL)
#
#     print(p.findall(S))
#     for size, m,y in p.findall(S):
#         if calc(size,m,y):
#             answer+=1
#     return answer

