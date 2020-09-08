import sys
sys.setrecursionlimit(10*6)

def solution(p):
    st=0
    ed=0
    valid=0
    check=[]

    if len(p)==0:
        return ""

    for idx in range(len(p)):
        if p[idx]=="(":
            st+=1
            check.append("(")
        else:
            ed+=1
            if check[-1]==")":
                valid=-1

        if st!=0 and ed!=0 and st==ed:
            break

    u=p[:idx+1]
    v=p[idx+1:]

    if sum==0:
        str=u+solution(v)
        return str
    else:
        str="("+solution(v)+")"+u[len(u)-1:1:-1]
        return str

if __name__=="__main__":
    p=input()
    print(solution(p))


