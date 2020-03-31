num=list(map(int, input().split()))
num.sort()
print(num[int(len(num)/2)])

# for i in range(len(num)-1):
#     try:
#         print(i)
#         if list[i] > list[i + 1]:
#             temp = list[i]
#             list[i] = list[i + 1]
#             list[i + 1] = temp
#     except:
#         break
# print(num[int(len(num)/2)])