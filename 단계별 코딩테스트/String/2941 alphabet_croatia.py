word=input()
croatian=["c=","c-","dz=","d-","lj","nj","s=","z="]

for i in croatian:
    word=word.replace(i,str(croatian.index(i)))
print(len(word))

# 코딩 후 참조하여 보니 대체로 단일 문자로 교체하는 경향의 코드들이 많았다.
# ex. 해당 문자들을 '0', 'a' 등으로 교체하는 방법들.