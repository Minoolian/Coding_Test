class Node:
    def __init__(self,w):
        self.word=w
        self.child={}
        self.length=0

class Trie:
    def __init__(self):
        self.root=Node(None)
        self.keyList={}

    def insert(self, words, rev):
        for word in words:
            if not rev:
                word=word[::-1]
            if word not in self.keyList:
                self.keyList[word]=len(word)
                cur_node=self.root

                for w in word:
                    if w not in cur_node.child:
                        cur_node.child[w]=Node(w)
                    cur_node=cur_node.child[w]
                cur_node.length=len(word)

    def search(self, word):
        num=0
        cur_node=self.root

        for w in word:
            if w not in cur_node.child:
                if w=='?':
                    stack=[]
                    l=len(word)
                    q_mark=word.count("?")
                    if q_mark==l:
                        for i in self.keyList.values():
                            if i==l:
                                num+=1
                        break

                    for node in cur_node.child.values():
                        stack.append((node,1))
                    while stack:
                        cur_node, cur_depth=stack.pop()
                        if cur_node.length==len(word) and cur_depth==q_mark:
                            num+=1

                        if cur_depth<q_mark:
                            for node in cur_node.child.values():
                                stack.append((node,cur_depth+1))
                    break
                else:
                    break
            cur_node=cur_node.child[w]
        return num

def solution(words, queries):
    answer=[]
    dic={}

    trie=Trie()
    trie.insert(words,True)

    r_trie=Trie()
    r_trie.insert(words,False)

    for q in queries:
        if q not in dic:
            if q.startswith('?'):
                answer.append(r_trie.search(q[::-1]))
            else:
                answer.append(trie.search(q))

        else:
            answer.append(dic[q])
    return answer


if __name__=="__main__":
