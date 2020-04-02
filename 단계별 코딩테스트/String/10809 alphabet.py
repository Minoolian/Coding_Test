S=list(input())

for i in range(ord('a'),ord('z')+1): #ascii 로 a~z 구현
    try:
        print(S.index(chr(i)),end=" ") #chr로 다시 변환
    except:
        print(-1,end=" ")
