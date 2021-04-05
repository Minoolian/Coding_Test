# 중위순회

# 재귀호출을 이용한 풀이
# https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=3&problemLevel=4&problemLevel=5&contestProbId=AV140YnqAIECFAYD&categoryId=AV140YnqAIECFAYD&categoryType=CODE&problemTitle=&orderBy=RECOMMEND_COUNT&selectCodeLang=PYTHON&select-1=5&pageSize=30&pageIndex=2

def inorder(cur):
    global result

    if not cur:
        return

    inorder(int(t[cur][1]))
    result+=t[cur][0]
    inorder(int(t[cur][2]))


for tc in range(1,11):

    n=int(input())
    t=[[] for _ in range(n+1)]
    result=""
    for i in range(n):
        inp=input().split()
        for j in range(1, 4):
            if j<len(inp):
                t[int(inp[0])].append(inp[j])
            else:
                t[int(inp[0])].append(0)

    inorder(1)
    print(f"#{tc} {result}")


