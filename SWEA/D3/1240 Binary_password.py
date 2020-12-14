# 단순 2진 암호코드

# List Slicing 풀이.
# https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV15FZuqAL4CFAYD&categoryId=AV15FZuqAL4CFAYD&categoryType=CODE



def trans(a):
    if a=='0001101': return 0
    elif a=='0011001': return 1
    elif a=='0010011': return 2
    elif a=='0111101': return 3
    elif a=='0100011': return 4
    elif a=='0110001': return 5
    elif a=='0101111': return 6
    elif a=='0111011': return 7
    elif a=='0110111': return 8
    elif a=='0001011': return 9

t=int(input())

for tc in range(1, t+1):
    n,m=map(int,input().split())

    barc=[input() for _ in range(n)]

    for tmp in barc:
        if '1' in tmp:
            tmp=tmp[::-1]
            for i in range(m):
                if tmp[i]=='1':
                    decode=tmp[i:i+56]
                    decode=decode[::-1]
                    break
            break

    result=[]
    comp=0
    for j in range(8):
        num=trans(decode[7*j:(7*j)+7])
        result.append(num)

        if j==7 and (comp+num)%10==0:
            print("#{} {}".format(tc, sum(result)))
            break
        elif j==7 and (comp+num)%10!=0:
            print("#{} {}".format(tc,0))
            break

        if j%2==0:
            comp+=(num*3)
        else:
            comp+=num