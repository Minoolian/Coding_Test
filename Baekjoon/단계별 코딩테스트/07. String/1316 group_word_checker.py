n=int(input())
count=0
for i in range(n):
    st=list(input())
    err=0
    while(len(st)!=0):
        rem = st[len(st)-1]
        for j in range(st.count(rem)):
            if rem==st[len(st)-1]:
                st.pop()
            else:
                err += 1
                st.remove(rem)
    if err == 0:
        count += 1

print(count)

# 1) https://leedakyeong.tistory.com/entry/%EB%B0%B1%EC%A4%80-1316%EB%B2%88-%EA%B7%B8%EB%A3%B9-%EB%8B%A8%EC%96%B4-%EC%B2%B4%EC%BB%A4-in-python
# 찾아낸 단어 순으로 정렬하여 두 문자열을 비교.
# cnt = 0
# for i in range(int(input)):
#     word = input()
#     cnt += list(word) == sorted(word, key=word.find)
# print(cnt)

# 2) https://aisiunme.github.io/algorithm/2018/08/13/baekjoon-group-word-checker-1316.md/
#  앞의 두글자를 비교해가며  find 했을때 중복된다면 앞에서 나타날 것이므로 앞의 값이 커지게 된다
# result = int(input())
# for _ in range(result):
#     word = input()
#     for i in range(1, len(word)):
#         if word.find(word[i-1]) > word.find(word[i]):
#             result -= 1
#             break
# print(result)
