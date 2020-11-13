# 링

#링의 반지름이 주어진다. 이때, 첫 번째 링을 한 바퀴 돌리면, 나머지 링은 몇 바퀴 돌아가는지 구하는 프로그램을 작성하시오.
import math

n=int(input())
ring=list(map(int,input().split()))

for i in range(1,n):
    gcd=math.gcd(ring[0],ring[i])
    print(ring[0]//gcd,"/",ring[i]//gcd,sep=""  )
    # 기약분수는 분모와 분자에 최대 공약수를 나눈 값
    # print('{0}/{1}'.format(ring[0]//gcd, ring[i]//gcd))