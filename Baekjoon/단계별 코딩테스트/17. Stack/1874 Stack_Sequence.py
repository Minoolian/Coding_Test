# 스택 수열

# 1부터 n까지의 수를 스택에 넣었다가 뽑아 늘어놓음으로써, 하나의 수열을 만들 수 있다.
# 이때, 스택에 push하는 순서는 반드시 오름차순을 지키도록 한다고 하자.
# 임의의 수열이 주어졌을 때 스택을 이용해 그 수열을 만들 수 있는지 없는지, 있다면 어떤 순서로 push와 pop 연산을 수행해야 하는지를 알아낼 수 있다.

# 입력된 수열을 만들기 위해 필요한 연산을 한 줄에 한 개씩 출력한다. push연산은 +로, pop 연산은 -로 표현하도록 한다. 불가능한 경우 NO를 출력한다.

n=int(input())
lis=[int(input()) for _ in range(n)]
temp=[0]
result=[]
a=1

for i in lis:
    while a<=n+1:
        if i!=temp[-1]:
            temp.append(a)
            a+=1
            result.append("+")
        else:
            temp.pop()
            result.append("-")
            break

if len(temp)==1:
    for i in result:
        print(i)
else:
    print("NO")


