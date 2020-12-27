# String

# List를 이용한 풀이.
# https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV14P0c6AAUCFAYi&categoryId=AV14P0c6AAUCFAYi&categoryType=CODE

# Trie 알고리즘을 이용한 풀이

# List를 이용한 풀이
for _ in range(10):
    n=int(input())
    f=input()
    s=input()

    result=0
    for i in range(len(s)):
        if s[i:i+len(f)]==f and i+len(f)<=len(s):
            result+=1

    print("#{} {}".format(n,result))
