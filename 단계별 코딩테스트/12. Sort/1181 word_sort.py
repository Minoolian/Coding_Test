N=int(input())
word_list=[]

for _ in range(N):
    word = input()
    word_len = len(word)
    word_list.append((word, word_len))

word_list=list(set(word_list))
# set은 hash 가능해야 하므로 문자열, 숫자, 튜플로 이루어져야 중복 제거 가능

word_list.sort(key=lambda x: (x[1],x[0]))

for i in word_list:
    print(i[0])
