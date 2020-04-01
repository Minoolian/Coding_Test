n=int(input())
a=list(map(int,input().split()))

print("%.2f" %((sum(a))/(n*max(a))*100)) #C와 유사하게 표현(소수점표현)