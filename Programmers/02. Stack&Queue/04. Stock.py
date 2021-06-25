# 주식가격

# 큐를 이용한 풀이
# https://programmers.co.kr/learn/courses/30/lessons/42584

import collections

def solution(prices):
    answer = []

    prices=collections.deque(prices)
    while prices:
        result=0
        check=prices.popleft()
        for i in prices:
            if check<=i:
                result+=1
            else:
                result+=1
                break
        answer.append(result)

    return answer