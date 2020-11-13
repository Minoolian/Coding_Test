A,B,C=map(int,input().split())

if B>=C:
    print(-1)
else:
    print(int(A/(C-B)+1))

# 반복문은 수행시간이 길다. 단순 식으로 변경 필요
# A,B,C=map(int,input().split())
# n=0
#
# if B>=C:
#     print(-1)
# else:
#     while True:
#         if (A+(B*n)) < (C*n):
#             print(n)
#             break
#         else:
#             n+=1