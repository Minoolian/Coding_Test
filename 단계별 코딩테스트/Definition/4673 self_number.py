not_self_num=set() # 1500ms
def d(n):
    new=0
    if(n<=10000):
        not_self_num.add(n)
        temp=list(str(n))
        for i in temp:
            new+=int(i)
        d(new+n)

self_num=[]
for j in range(1,10001):
    if list(not_self_num).count(j)==0:
        self_num.append(j)
        d(j)

for i in self_num:
    print(i)
################# 1) 아래와 같은 맥락 // 600ms
# def d(n):
#     a = 0
#     for x in list(str(n)):
#         a = a + int(x)
#     return int(n) + a
# a= []
# for i in range(1,10001):
#     k = d(i)
#     a.append(k)
#
# for b in range(1, 10001):
#     if b in a:
#         pass
#     else:
#         print(b)

################# 2) 전체집합 - not_self__num = self_num // 재귀 X // 68ms
# num = set(range(1,10001))
# generated_num = set()
# for i in range(1,10001):
#     for j in str(i):
#         i += int(j)
#     generated_num.add(i)
# self_num = num - generated_num
# for k in sorted(self_num):
#     print(k)