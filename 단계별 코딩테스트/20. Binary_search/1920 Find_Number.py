# 수 찾기

# N개의 정수 A[1], A[2], …, A[N]이 주어져 있을 때, 이 안에 X라는 정수가 존재하는지 알아내는 프로그램

def binary(arr, val, low, high):
    if low>high:
        return False

    mid=(low+high)//2
    if val>arr[mid]:
        return binary(arr, val, mid+1, high)
    elif val<arr[mid]:
        return binary(arr, val, low, mid-1)
    else:
        return True

n=int(input())
a=list(map(int,input().split()))
m=int(input())
b=list(map(int,input().split()))

a.sort()

for i in b:
    if binary(a, i, 0, n-1):
        print(1)
    else:
        print(0)
