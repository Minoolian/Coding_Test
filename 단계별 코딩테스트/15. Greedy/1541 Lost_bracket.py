# 잃어버린 괄호

# 양수와 +, -, 그리고 괄호를 가지고 길이가 최대 50인 식을 만들었다. 그리고 나서 괄호를 모두 지웠다.
# 그리고 나서 괄호를 적절히 쳐서 이 식의 값을 최소로 만들려고 한다.

lis=input().split('-')
result=0

for i in lis[0].split('+'): # 첫번째 집합은 +연산
    result+=int(i)

for i in lis[1:]: # 두번째 집합부터 - 연산
    for j in i.split('+'):
        result-=int(j)

print(result)