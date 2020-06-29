import sys

n=int(sys.stdin.readline())
h=[]
hlen=0

while n>0:
    n-=1
    x=int(sys.stdin.readline())
    if x>0: # push (리프부터 루트로)
        h.append(x)
        hlen+=1
        end=hlen-1

        while end>0:
            if h[end]<h[(end-1)//2]: # 부모노드보다 자식노드의 값이 크면
                h[end],h[(end-1)//2]=h[(end-1)//2],h[end] # 스위치
                end=(end-1)//2 # 부모노드 갱신
            else:
                break

    elif x==0: # pop (루트부터 리프로)
        if hlen==0: # 비어있을 경우 0 출력
            print(0)
        else:
            print(h[0])
            h[0]=h[hlen-1]
            h.pop() # 루트노드와 제일 마지막노드를 바꾼 후 삭제
            hlen-=1
            p=0 # 부모노드 시작 인덱스
            c=1 # 자식노드 시작 인덱스

            while c<=hlen-1:
                if p*2+2<=hlen-1 and h[p*2+1]>h[p*2+2]: # 자식 노드 중 작은 것을 변수 c로 설정
                    c=p*2+2

                if h[c]<h[p]: # 자식노드가 부모노드보다 작다면 (최소힙)
                    h[c],h[p]=h[p],h[c]
                    p=c
                    c=p*2+1 # 자식노드 변경
                else:
                    break
