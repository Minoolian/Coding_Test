# 진기의 최고급 붕어빵

# 단순 수학계산 문제
# https://dheldh77.tistory.com/entry/SWEA-1860-%EC%A7%84%EA%B8%B0%EC%9D%98-%EC%B5%9C%EA%B3%A0%EA%B8%89-%EB%B6%95%EC%96%B4%EB%B9%B5?category=790689?category=790689

t=int(input())

for tc in range(1, t+1):
    n,m,k=map(int,input().split())
    cus=list(map(int,input().split()))

    cus.sort()

    result="Possible"
    for i in range(len(cus)):
        if k*(cus[i]//m)<i+1:
            result="Impossible"
            break

    print("#{} {}".format(tc, result))