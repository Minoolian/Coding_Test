t=int(input())
for i in range(t):
    a, b = map(str, input().split())
    for j in str(b):
        print(j*int(a),end="")
    print()