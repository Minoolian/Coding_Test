# 문자열 집합

# 첫째 줄에 문자열의 개수 N과 M
# 다음 N개의 줄에는 집합 S에 포함되어 있는 문자열들
# 다음 M개의 줄에는 검사해야 하는 문자열들
#
# 첫째 줄에 M개의 문자열 중에 총 몇 개가 집합 S에 포함되어 있는지 출력

import sys
input=sys.stdin.readline

class Node:
    def __init__(self, key, data):
        self.key=key
        self.data=data
        self.child={}

class Trie:
    def __init__(self):
        self.root=Node(None)

    def insert(self, string):
        cur_node=self.root

        for s in string:
            if s not in cur_node.child:
                cur_node.child[s]=Node(s)
            cur_node=cur_node.child[s]

        cur_node.data=string

    def search(self, string):
        cur_node=self.root

        for s in string:
            if s in cur_node.child:
                cur_node=cur_node.child[s]
            else
                return False

        if cur_node.data:
            return True
        return False

if __name__ =="__main__":
    n,m=map(int,input().split())
    trie=Trie()
    cnt=0

    for i in range(n+m):
        string=input().rstrip()
        if i<n:
            trie.insert(string)
        else:
            if trie.search(string):
                cnt+=1

    print(cnt)