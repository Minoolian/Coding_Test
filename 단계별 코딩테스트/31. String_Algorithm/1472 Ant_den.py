# 개미굴

# 첫 번째 줄은 로봇 개미가 각 층을 따라 내려오면서 알게 된 먹이의 정보 개수 N개
# 두 번째 줄부터 N+1 번째 줄까지, 각 줄의 시작은 로봇 개미 한마리가 보내준 먹이 정보 개수 K
# 다음 K개의 입력은 로봇 개미가 왼쪽부터 순서대로 각 층마다 지나온 방에 있는 먹이 정보이며 먹이 이름 길이 t
#
# 개미굴의 시각화된 구조를 출력하여라.

# 트라이 알고리즘을 이용하지 않은 풀이
N=int(input())
ant=[]
 
for i in range(N):
    arr=list(input().split())
    ant.append(arr[1:])
 
ant.sort()
for i in range(N):
    if i==0:#첫배열
        for j in range(len(ant[i])):
            print("--"*j+ant[i][j])
    else:
        count=-1
        for j in range(len(ant[i])):#dfs
            if len(ant[i-1])<=j or ant[i-1][j]!=ant[i][j]: #이전배열과 같은지 비교
                break
            else:#같다면 출력하지 않고 넘어간다.
                count=j#어디까지 같은지 저장
        for j in range(count+1,len(ant[i])):#같은것을 제외한 나머지 인자 출력
            print("--" * j + ant[i][j])