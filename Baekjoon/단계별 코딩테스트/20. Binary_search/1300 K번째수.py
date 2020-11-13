# K번 째 수

# NXN 배열 A가 있다. 배열에 들어있는 수는 A[i][j] = i×j 이다.
# 이 수를 일차원 배열 B에 넣으면 B의 크기는 NXN 개가 된다. B를 오름차순 정렬했을 때, B[k]를 구해보자

# NXN 행렬을 만들어 오름차순 정렬하는 것은 시간이 효율적이지 않다.

N, K = int(input()), int(input())
start, end = 1, K

while start <= end:
    mid = (start + end) // 2

    temp = 0
    for i in range(1, N + 1):
        temp += min(mid // i, N)
    # 어떤 수(mid) 보다 작거나 같은 자연수의 곱(i*j) 가 몇개인 지 알아내면 mid가 몇번째 수인지 알 수 있다.
    # 어떤 특정한 수 보다 작은 수의 갯수는 그 수에 모든 행을 나눈 몫들의 합이다.

    if temp >= K:  # 구한 값이 구하려는 값보다 크거나 같다면 이진탐색을 작은 구간에서 시행한다.
        answer = mid
        end = mid - 1
    else:
        start = mid + 1
print(answer)