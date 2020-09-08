import sys
input=sys.stdin.readline

def solution(s):

    l=len(s)
    leng=l//2+1
    min_num=1000

    for i in range(1,leng+1):
        answer=""
        start=0
        check=""
        cnt=1
        while start<=l:
            if start+i>l:
                answer+=s[start:]

            tmp=s[start:start+i]
            if start==0:
                check=tmp
            elif check!=tmp:
                if cnt==1:
                    answer+=check
                else:
                    answer+=str(cnt)+check
                check=tmp
                cnt=1
            else:
                cnt+=1

            start+=i

        min_num=min(min_num,len(answer))

    return min_num

if __name__== "__main__":
    s=input().rstrip()
    print(solution(s))