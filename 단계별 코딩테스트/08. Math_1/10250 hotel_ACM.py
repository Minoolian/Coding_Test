T = int(input())

for _ in range(T): # 변수가 필요치 않을 경우 언더바 처리해도 무관
    H, W, N = map(int, input().split())
    a = 1

    while True:
        if N <= H * a:
            floor = H - (H * a - N)
            break
        else:
            a += 1
    if a < 10:
        print(floor, 0, a, sep="")
    else:
        print(floor, a, sep="")

# https://pacific-ocean.tistory.com/125
# 반복문이 없이 더욱 간결 n과 h의 관계로 풀이
# t = int(input())
# for i in range(t):
#     h, w, n = map(int, input().split())
#     f = 0
#     ho = 0
#     if n % h == 0: # 층수로 나누어 떨어진다면
#         f = h * 100 # 최고높이가 층수
#         ho = n // h # +1 필요없이 몫 자체가 호수
#     else:
#         f = (n % h) * 100 # 나머지는 층수
#         ho = 1 + n // h # 몫의 +1 은 호수
#     print(f + ho)