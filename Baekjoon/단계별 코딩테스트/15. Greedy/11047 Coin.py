# 동전 0

# 동전은 총 N종류이고, 각각의 동전을 매우 많이 가지고 있다.
# 동전을 적절히 사용해서 그 가치의 합을 K로 만들려고 한다. 이때 필요한 동전 개수의 최솟값을 구하라.

n, v= map(int, input().split())
coin=[int(input()) for _ in range(n)]
result=0

for i in range(n-1,-1,-1):
    if v//coin[i]:
        result+=v//coin[i]
        v=v%coin[i]

print(result)