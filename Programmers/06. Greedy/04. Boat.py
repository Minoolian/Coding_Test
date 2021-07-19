# 구명보트

# 리스트를 이용한 풀이
# https://programmers.co.kr/learn/courses/30/lessons/42885

def solution(people, limit):
    answer = 0
    
    people.sort(reverse=True)
    left,right=0,len(people)-1
    
    while left<=right:
        if people[left]+people[right]<=limit:
            left+=1
            right-=1
        else:
            left+=1
            
        answer+=1
            
    return answer