# 괄호

# 괄호 문자열(Parenthesis String, PS)은 두 개의 괄호 기호인 ‘(’ 와 ‘)’ 만으로 구성되어 있는 문자열
# 괄호의 모양이 바르게 구성된 문자열을 올바른 괄호 문자열(Valid PS, VPS)
# 주어진 괄호 문자열이 VPS 인지 아닌지를 판단해서 그 결과를 YES 와 NO

def check(lis):
    sum=0
    for i in lis:
        if i=='(':
            sum+=1
        else:
            sum-=1

        if sum<0:
            print("NO")
            return
    if sum>0:
        print("NO")
    elif sum==0:
        print("YES")

n=int(input())

for _ in range(n):
    lis=input()
    check(lis)

