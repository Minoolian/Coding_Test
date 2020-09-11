def rev(s):
    str=""
    for x in s:
        if x=="(":
            str+=")"
        else:
            str+="("
    return str

def solution(p):
    st=0
    ed=0
    valid=0
    sum=0

    if len(p)==0:
        return ""

    for idx in range(len(p)):
        if p[idx]=="(":
            st+=1
            sum+=1
        else:
            ed+=1
            sum-=1

        if sum<0:
            valid=-1

        if st!=0 and ed!=0 and st==ed:
            break

    u=p[:idx+1]
    v=p[idx+1:]

    if valid==0:
        str1=u+solution(v)
        return str1
    else:
        str2="("+solution(v)+")"+rev(u[1:-1])
        return str2

if __name__=="__main__":
    p=input()
    print(solution(p))


