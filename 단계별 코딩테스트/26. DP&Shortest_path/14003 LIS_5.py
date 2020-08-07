# 가장 긴 증가하는 부분 수열5

# 수열 A가 주어졌을 때, 가장 긴 증가하는 부분 수열을 구하는 프로그램을 작성
# 예를 들어, 수열 A = {10, 20, 10, 30, 20, 50} 인 경우에 가장 긴 증가하는 부분 수열은 A = {10, 20, 10, 30, 20, 50} 이고, 길이는 4

import bisect

def lis(arr):
    lis_arr = [arr[0]]
    res = [0]
    for n in arr[1:]:
        if lis_arr[-1] < n:
            lis_arr.append(n)
            res.append(len(lis_arr)-1)
        else:
            where = bisect.bisect_left(lis_arr, n)
            lis_arr[where] = n
            res.append(where)

    i = len(lis_arr)
    print(i)
    ans = []
    for idx in range(len(res)-1, -1, -1):
        if res[idx] == i-1:
            ans.append(arr[idx])
            i -= 1
    print(*ans[::-1])

input()
lis(list(map(int, input().split())))