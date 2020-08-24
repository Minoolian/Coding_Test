# 트리의 부모
# 트리의 루트를 1이라고 정했을 때, 각 노드의 부모를 구하는 프로그램

# 부모만을 찾는 코드(Tree 구성 X)
import sys
sys.setrecursionlimit(10 ** 9) # 재귀 함수의 깊이 설정
 
N=int(sys.stdin.readline())#노드의 갯수
tree=[[] for _ in range(N+1)]
for _ in range(N-1):
    s,e=map(int,sys.stdin.readline().split())
    tree[s].append(e)
    tree[e].append(s)
 
 
#부모저장
parents=[0 for _ in range(N+1)]
 
 
def DFS(start,tree,parents):
    for i in tree[start]:#연결된 노드 모두탐색
        if parents[i]==0:#한번도 방문한적이 없다면
           parents[i]=start#부모노드 저장
           DFS(i,tree,parents)
 
 
DFS(1,tree,parents)
 
for i in range(2,N+1):
    print(parents[i])