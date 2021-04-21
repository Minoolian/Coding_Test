from itertools import combinations

def comb(orders, course, result):
    for i in range(len(course)):
        for c in combinations(sorted(orders),course[i]):
            if c in result[i].keys():
                result[i][c]+=1
            else:
                result[i][c]=1
    return result

def solution(orders, course):
    result = [{} for _ in range(len(course))]
    answer = []

    for order in orders:
        result=comb(order, course, result)

    for re in result:
        for key, value in re.items():
            if value==max(re.values()) and value>1:
                answer.append(''.join(key))


    return sorted(answer)