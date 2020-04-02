n=int(input())
count=0

for i in range(1,n+1):
    if i<100:
        count+=1
    else:
        count+=1
        slice=list(str(i))
        gap=int(slice[1])-int(slice[0])
        for j in range(len(slice)-1):
            if gap!=(int(slice[j+1])-int(slice[j])):
                count-=1
                break
print(count)


# https://roseline124.github.io/algorithm/2019/03/29/Algorithem-baekjoon-1065.html
# 1000 이하의 수가 제약되어 있기때문에 더욱 간단하게 가능
# num = int(input())
# hansu = 0
#
# for n in range(1, num + 1):
#     if n <= 99:  # 1부터 99까지는 모두 한수
#         hansu += 1
#
#     else:
#         nums = list(map(int, str(n)))  # 숫자를 자릿수대로 분리
#         if nums[0] - nums[1] == nums[1] - nums[2]:  # 등차수열 확인
#             hansu += 1