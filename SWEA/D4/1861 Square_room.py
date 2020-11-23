# 정사각형 방

# DFS를 이용한 풀이.
# https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV5LtJYKDzsDFAXc&categoryId=AV5LtJYKDzsDFAXc&categoryType=CODE

def dfs(x,y):

    result=0
    for i in range(4):
        nx=x+i_x[i]
        ny=y+i_y[i]

        if nx>=0 and nx<n and ny>=0 and ny<n:
            if room[x][y]+1==room[nx][ny]:
                result=max(result,dfs(nx,ny)+1)

    if result==0: return 1
    else: return result

if __name__=="__main__":

    i_x=[1,0,-1,0]
    i_y=[0,1,0,-1]

    t=int(input())
    for tc in range(1, t+1):
        n=int(input())
        room=[list(map(int,input().split())) for _ in range(n)]


        idx=[]
        m=0
        for i in range(n):
            for j in range(n):
                move=dfs(i,j)
                if move==m or m==0:
                    idx.append(room[i][j])
                    m=move
                elif move>m:
                    idx=[room[i][j]]
                    m=move
        idx.sort()
        print("#{} {} {}".format(tc, idx[0], m))


