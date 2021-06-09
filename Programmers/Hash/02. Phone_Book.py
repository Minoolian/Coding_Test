# 전화번호 목록

# Trie 알고리즘을 이용한 풀이
# https://programmers.co.kr/learn/courses/30/lessons/42577

class Node():
    def __init__(self, key):
        self.data=key
        self.child={}
        self.exist=None

class Trie():
    def __init__(self):
        self.root=Node(None)

    def insert(self, string):
        cur_node=self.root

        for s in string:
            if cur_node.exist:
                return False

            if s not in cur_node.child:
                cur_node.child[s]=Node(s)
            cur_node=cur_node.child[s]

        if cur_node.child:
            return False

        cur_node.exist=string
        return True

def solution(phone_book):
    answer = True
    trie=Trie()

    for number in phone_book:
        if not trie.insert(number):
            answer=False
            break

    return answer

# Sort와 startswith 메서드를 이용한 타인 풀이 (시간복잡도 면에서 손해)

# def solution(phoneBook):
#     phoneBook = sorted(phoneBook)
#
#     for p1, p2 in zip(phoneBook, phoneBook[1:]):
#         if p2.startswith(p1):
#             return False
#     return True