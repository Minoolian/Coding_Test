n=int(input())

for i in range(1,2*n+1):
    for j in range(1,n+1):
        if i%2!=0:
            if j%2!=0:
                print("*",end="")
            else:
                print(" ",end="")
        else:
            if j%2!=0:
                print(" ",end="")
            else:
                print("*",end="")
    print("")

    # https://somewheretogo.tistory.com/112
    # N = int(input())
    # even = N // 2
    # odd = N - N // 2
    #
    # for i in range(N):
    #     print("* " * odd)
    #     print(" *" * even)