a=input().split()
print(len(a))

# 1) 이 풀이의 경우 단어 자체가 공백인 경우도 계산하기에 실패
# s=input()
# s.strip()
# count=[]
#
# for i in range(s.count(" ")):
#     count.append(s[:s.index(" ")])
#     s=s[s.index(" ")+1:]
# count.append(s)
#
# print(len(count))

# 2) 앞과 뒤의 공백을 삭제하는 코드를 포함
# n = list(input().split(' '))
#
# print(n)
# while '' in n:
#     n.remove('')
# print(n)
#
# if len(n) < 1000000:
#     print(len(n))