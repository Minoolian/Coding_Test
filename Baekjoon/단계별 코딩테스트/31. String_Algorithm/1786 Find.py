# 찾기

# 두 개의 문자열 P와 T에 대해, 문자열 P가 문자열 T 중간에 몇 번, 어느 위치에서 나타나는지 알아내는 문제

# 첫째 줄에 문자열 T가, 둘째 줄에 문자열 P가 주어진다.
# 첫째 줄에, T 중간에 P가 몇 번 나타나는지를 나타내는 음이 아닌 정수를 출력한다. 둘째 줄에는 P가 나타나는 위치를 차례대로 공백으로 구분해 출력한다.

import sys
input=sys.stdin.readline

t=input().rstrip() # sys.stdin.readline() 시 개행문자가 삽입되므로 주의
p=input().rstrip()

pi=[0 for i in range(len(p))]

j=0
for i in range(1, len(p)):
    while j>0 and p[i]!=p[j]:
        j=pi[j-1]

    if p[i]==p[j]:
        j+=1
        pi[i]=j

result=[]
count=0
j=0
for i in range(len(t)):
    while j>0 and t[i]!=p[j]:
        j=pi[j-1]

    if t[i]==p[j]:
        if j==len(p)-1:
            result.append(i-len(p)+2)
            count+=1
            j=pi[j]
        else:
            j+=1

print(count)
for i in result:
    print(i)