N=int(input())

for i in range(N):
    result = i + sum([int(j) for j in str(i)])
    if result==N:
        print(i)
        exit(0)
print(0)
