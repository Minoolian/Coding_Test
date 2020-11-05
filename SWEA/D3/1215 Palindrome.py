# 회문

#
# https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV14QpAaAAwCFAYi&categoryId=AV14QpAaAAwCFAYi&categoryType=CODE&&&

# 반복문을 이용한 풀이
for tc in range(1, 11):
    n=int(input())
    result=0
    lis=[input() for _ in range(8)]
    rev_lis=list(map(list, zip(*lis)))

    for i in range(8):
        for j in range(9-n):
            horiz=lis[i][j:j+n]
            verti=rev_lis[i][j:j+n]

            if horiz==horiz[::-1]:
                result+=1
            if verti==verti[::-1]:
                result+=1

    print("#{} {}".format(tc, result))

    



# DP를 이용한 풀이
# def reverse(temp):
#     lis=[[] for _ in range(8)]
#     idx=0
#
#     for i in temp:
#         for a in i:
#             lis[idx].append(a)
#             idx+=1
#         idx=0
#
#     return lis
#
#
# def palindrome(temp):
#     result=0
#
#     for lis in temp:
#         dp=[[0]*(8) for _ in range(8)]
#
#         for i in range(8): # 길이가 1인 경우는 모두 팰린드롬
#             dp[i][i]=1
#             if n==1:
#                 result+=1
#
#         for i in range(7): # 길이가 2인 경우는 확인 후 팰린드롬
#             if lis[i]==lis[i+1]:
#                 dp[i][i+1]=1
#             if n==2:
#                 result+=1
#
#         for i in range(2,n): # 길이가 3이상인 경우도 확인 후 팰린드롬
#             for j in range(8-i):
#                 if lis[j]==lis[j+i] and dp[j+1][j+i-1]==1:
#                     # 이미 이전의 길이들은 팰린드롬인 지 확인했기에 그것을 토대로 검사
#                     dp[j][j+i]=1
#                     if i==(n-1):
#                         result+=1
#     return result
#
# if __name__=="__main__":
#
#     for tc in range(1, 11):
#         n=int(input())
#         temp=[]
#         for _ in range(8):
#             temp.append(input())
#
#         print("#{} {}".format(tc, palindrome(temp)+palindrome(reverse(temp))))