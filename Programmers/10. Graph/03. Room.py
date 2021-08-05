# 방의 개수

# 그래프 탐색을 이용한 풀이
# https://programmers.co.kr/learn/courses/30/lessons/49190
import collections

dx=[1,1,0,-1,-1,-1,0,1]
dy=[0,1,1,1,0,-1,-1,-1]

# 오일러의 다면체 정리로 푸는 방법도 존재 v-e+f=1 (2차원) vortex, edge, face
def solution(arrows):
    answer=0
    visit,visit_dir=collections.defaultdict(bool),collections.defaultdict(bool)

    cur=(0,0)
    q=collections.deque([cur])
    for i in arrows:
        for _ in range(2): # 교차부분 해결을 위해 두칸씩 이동
            next=(cur[0]+dx[i],cur[1]+dy[i])
            q.append(next)

            cur=next

    cur=q.popleft()
    visit[cur]=True

    while q:
        next=q.popleft()

        if visit[next]:
            if not visit_dir[(cur,next)]:
                answer+=1
        else:
            visit[next]=True

        visit_dir[(cur,next)]=True
        visit_dir[(next,cur)]=True
        cur=next

    return answer

print(solution([6, 6, 6, 4, 4, 4, 2, 2, 2, 0, 0, 0, 1, 6, 5, 5, 3, 6, 0]))