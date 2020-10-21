# View

# 간단한 배열 응용문제
# https://swexpertacademy.com/main/code/problem/problemSubmitHistory.do?contestProbId=AV134DPqAA8CFAYh

for test_case in range(1, 11):
    n=int(input())
    building=list(map(int,input().split()))

    result=0
    for i in range(2, n-2):
        top=max(building[i-2],building[i-1],building[i+1],building[i+2])
        if building[i]>top: result+=(building[i]-top)

    print("#%d"%test_case,result)