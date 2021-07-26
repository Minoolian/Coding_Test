# 도둑질

# DP를 이용한 풀이
# https://programmers.co.kr/learn/courses/30/lessons/42897

def solution(money):
    dp=[0]*len(money)
    dp[0]=money[0]
    dp[1]=max(dp[0],money[1])

    for i in range(2,len(money)-1):
        dp[i]=max(dp[i-1],money[i]+dp[i-2])

    dp2=[0]*len(money)
    dp2[1]=money[1]

    for i in range(2,len(money)):
        dp2[i]=max(dp2[i-1],money[i]+dp2[i-2])


    return max(max(dp),max(dp2))


# 리스트 없는 타인 풀이
# def solution(a):
#     x1, y1, z1 = a[0], a[1], a[0]+a[2]
#     x2, y2, z2 = 0, a[1], a[2]
#     for i in a[3:]:
#         x1, y1, z1 = y1, z1, max(x1, y1)+i
#         x2, y2, z2 = y2, z2, max(x2, y2)+i
#     return max(x1, y1, y2, z2)