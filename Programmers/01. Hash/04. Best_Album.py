# 베스트앨범

# Dictionary를 이용한 풀이
# https://programmers.co.kr/learn/courses/30/lessons/42579

def solution(genres, plays):
    answer = []

    gen={g:0 for g in set(genres)}
    play={g:[] for g in set(genres)}

    for idx, value in enumerate(zip(genres, plays)):
        play[value[0]].append([value[1],idx])
        gen[value[0]]+=value[1]

    for g,p in sorted(gen.items(), key=lambda x:x[1], reverse=True):
        play[g].sort(key=lambda x:(x[0],-x[1]), reverse=True)
        answer=answer+[play[g][i][1] for i in range(len(play[g])) if i<2]


    return answer