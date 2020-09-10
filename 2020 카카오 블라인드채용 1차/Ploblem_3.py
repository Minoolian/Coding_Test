
def right():
def left():
def up():
def down():

def rotate(lis): # 90도 회전
    n=len(lis[0])
    new=[[None]*n for _ in range(n)]

    for i in range(n):
        for j in range(n):
            new[j][n-1-i]=lis[i][j]

    return new

def solution(key, lock):
    answer = True
    return answer

if __name__=="__main__":
    key=[[0, 0, 0], [1, 0, 0], [0, 1, 1]]
    lock=[[1, 1, 1], [1, 1, 0], [1, 0, 1]]

    print(solution(key,lock))