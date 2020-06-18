import sys
n=int(input())
paper=[(sys.stdin.readline().rstrip()) for _ in range(n)]

print(paper)
print(paper[0][1])