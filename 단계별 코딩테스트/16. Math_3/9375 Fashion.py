# 패션왕 신해빈

# 첫째줄은 테스트케이스
# 각 테스트 케이스의 첫째 줄에는 해빈이가 가진 의상의 수 n(0 ≤ n ≤ 30)이 주어진다.
# 다음 n개에는 해빈이가 가진 의상의 이름과 의상의 종류가 공백으로 구분되어 주어진다. 같은 종류의 의상은 하나만 입을 수 있다.

from collections import Counter

n=int(input())

for _ in range(n):
    k=int(input())
    lis = []
    for _ in range(k):
        a,b=input().split()
        lis.append(b)

    result=Counter(lis) #list 내의 값의 갯수를 key-value (딕셔너리)로 반환
    num=1

    for key in result:
        num *= result[key]+1
    print(num-1)
