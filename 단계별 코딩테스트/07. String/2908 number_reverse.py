a,b=map(list,input().split())
a.reverse() # reverse 메서드 자체를 호출하면 반환값은 None
b.reverse()
a="".join(a) # join 메서드: ""로 분리하여 리스트를 합침
b="".join(b)
if a>b:
     print(a)
else:
     print(b)


# https://roseline124.github.io/algorithm/2019/04/01/Altorithm-baekjoon-2908.html
# a, b = input().split()
#
# a = int(a[::-1]) // 문자열을 뒤집어주는 방법
# b = int(b[::-1])
#
# if a > b :
#     print(a)
# else :
#     print(b)