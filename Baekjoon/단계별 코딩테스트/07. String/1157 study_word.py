st=list(input().upper())
alpha={} # 딕셔너리를 활용해 보았다.
c=[]

for i in range(ord('A'),ord('Z')+1):
    alpha[chr(i)]=0

for i in st:
    alpha[i]+=1

for i,j in alpha.items(): # key,value 쌍 모두 불러들일 수 있다.
    if j==max(alpha.values()):
        c.append(i)
        if len(c)>1:
            print("?")
            break
if len(c)==1:
    print(c[0])


# https://hwiyong.tistory.com/155 리스트로만 이용한 방법
# words = input().lower()
# words_list = list(set(words))
# word_count = list()
#
# for i in words_list:
#     count = words.count(i)
#     word_count.append(count)
#
# if(word_count.count(max(word_count)) >= 2):
#     print('?')
# else:
#     print(words_list[(word_count.index(max(word_count)))].upper())

