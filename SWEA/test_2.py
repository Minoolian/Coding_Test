from collections import deque

def dist(s,v):
    d=abs(s[0]-v[0])+abs(s[1]-v[1])
    result= True if d>2 else False

    return result


def bfs(places):
    person=deque()
    idx_x=[1,0,-1,0]
    idx_y=[0,1,0,-1]

    for i in range(5):
        for j in range(5):
            if places[i][j]=='P':
                person.append([i,j,0])

    judge=True
    while judge and person:
        origin=person.popleft()
        q=deque()
        q.append(origin)

        visit=[[True]*5 for _ in range(5)]
        visit[origin[0]][origin[1]]=False
        while q and judge:
            x,y,d=q.popleft()
            for i in range(4):
                nx=x+idx_x[i]
                ny=y+idx_y[i]


                if (0<=nx<5 and 0<=ny<5) and places[nx][ny]!='X' and visit[nx][ny]:
                    if places[nx][ny]=='P':
                        if not d+1>2:
                            judge=False
                            break
                    q.append([nx,ny,d+1])
                    visit[nx][ny]=False


    return judge

def solution(places):
    answer=[]

    for case in places:
        a=1 if bfs(case) else 0
        answer.append(a)

    return answer

print(solution([["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"]]))