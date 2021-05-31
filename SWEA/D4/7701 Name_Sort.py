# 염라대왕의 이름 정렬

# 리스트 정렬을 이용한 풀이
# https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=3&problemLevel=4&problemLevel=5&contestProbId=AWqU0zh6rssDFARG&categoryId=AWqU0zh6rssDFARG&categoryType=CODE&problemTitle=&orderBy=SUBMIT_COUNT&selectCodeLang=PYTHON&select-1=5&pageSize=30&pageIndex=1

# 단순 풀이

t=int(input())
for tc in range(1, t+1):
    n=int(input())
    arr=[input() for _ in range(n)]

    arr=list(set(arr))
    arr.sort(key=lambda x:(len(x),x))
    print(f"#{tc}")
    for result in arr:
        print(result)

# 런타임 에러
# from collections import deque
#
# class Node:
#     def __init__(self, key):
#         self.key=key
#         self.child={}
#         self.word=None
#
# class Trie:
#     def __init__(self):
#         self.root=Node(None)
#
#     def insert(self, string_arr):
#         cur_node=self.root
#
#         for string in string_arr:
#             if string not in cur_node.child:
#                 cur_node.child[string]=Node(string)
#             cur_node=cur_node.child[string]
#         cur_node.word=string_arr
#
#     def bfs(self):
#         q=deque()
#         q.append(self.root)
#
#         while q:
#             cur_node=q.popleft()
#
#             if cur_node.word:
#                 print(cur_node.word)
#
#             for key in sorted(cur_node.child):
#                 q.append(cur_node.child[key])
#
#
# if __name__=="__main__":
#     t=int(input())
#     for tc in range(1, t+1):
#         n=int(input())
#         trie=Trie()
#
#         for _ in range(n):
#             trie.insert(input())
#
#         print(f"#{tc}")
#         trie.bfs()