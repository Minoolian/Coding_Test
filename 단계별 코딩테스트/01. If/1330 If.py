a, b = map(int, input().split()) #입력값 한줄에 받기

if a>b:
    print(">")
elif a<b:
    print("<")
else:
    print("==")