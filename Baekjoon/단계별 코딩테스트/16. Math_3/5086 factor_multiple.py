# 배수와 약수

# 두 수가 주어졌을 때, 다음 3가지 중 어떤 관계인지 구하는 프로그램을 작성하시오.
# 1. 첫 번째 숫자가 두 번째 숫자의 약수이다.
# 2. 첫 번째 숫자가 두 번째 숫자의 배수이다.
# 3. 첫 번째 숫자가 두 번째 숫자의 약수와 배수 모두 아니다.



while True:
    a, b = map(int, input().split())
    if a!=0 and b!=0:
        if b%a==0:
            print("factor")
        elif a%b==0:
            print("multiple")
        else:
            print("neither")
    else:
        break
