import sys
N=int(input())
kg_3=0

while (3*kg_3)<=N:
    if (N-(3*kg_3))%5 ==0:
        print(kg_3+(N-(3*kg_3))//5)
        sys.exit(0)
    else:
        kg_3+=1
print(-1)