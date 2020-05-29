# 회의실 배정

# 한 개의 회의실이 있는데 이를 사용하고자 하는 N개의 회의에 대하여 회의실 사용표를 만들려고 한다.
# 각 회의 I에 대해 시작시간과 끝나는 시간이 주어져 있고, 각 회의가 겹치지 않게 하면서 회의실을 사용할 수 있는 회의의 최대 개수를 찾아보자.

n=int(input())
meet=[list(map(int,input().split())) for _ in range(n)]

meet.sort(key=lambda x:(x[1],x[0])) # 끝시간정렬 후 시작시간 정렬
result=0
check=0

for i in meet:
    if check<=i[0]:
        result+=1
        check=i[1]

print(result)