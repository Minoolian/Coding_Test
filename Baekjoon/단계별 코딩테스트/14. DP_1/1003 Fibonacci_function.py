# 앞의예제 Fibonacci_2 를 DP로 풀었던 문제로 시도했던 것은 잘못되었다.
# memoization을 통해서 중복되는 과정을 삭제 했기 때문이다.
# 아래 방법은 0과 1을 카운트 하는 것 마저 피보나치의 성질을 갖는다는 것을 이용했다.
import sys
count_0=[1,0,1]
count_1=[0,1,1]

def fibo(n):
    if n>=len(count_0): # 여러 횟수를 거치므로, 단순히 숫자3으로 입력할 경우 append 시 3일때의 수가 계속 추가될 수 있다.
        for i in range(len(count_1),n+1):
            count_0.append(count_0[i-1]+count_0[i-2])
            count_1.append(count_1[i - 1] + count_1[i - 2])

    print(count_0[n],count_1[n])

for _ in range(int(sys.stdin.readline())):
    fibo(int(sys.stdin.readline()))