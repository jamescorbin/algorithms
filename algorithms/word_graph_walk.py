from typing import List

def check_distance_one(word1: str, word2: str) -> bool:
    """
    word1 and word2 are same length
    """
    miss = 0
    for i in range(len(word1)):
        if word1[i] != word2[i]:
            miss += 1
        if miss > 1:
            break
    return True if miss == 1 else 0

class Node():
    def __init__(self, val: str):
        self.val = val
        self.neigh = list()

class Graph():
    def __init__(self):
        self.nodes = dict()

    def add(self, node: Node) -> None:
        for word, nd in self.nodes.items():
            if check_distance_one(word, node.val):
                nd.neigh.append(node)
                node.neigh.append(nd)
        self.nodes[node.val] = node

    def get_distance(self, start_word: str, target: str) -> int:
        buffer = [self.nodes[start_word]]
        hashset = set([nd.val for nd in buffer])
        p0 = 0
        p1 = p0
        level = 0
        ret = 0
        while p0 < len(buffer):
            nxt = buffer[p0]
            to_add = [nd for nd in nxt.neigh if nd not in hashset]
            buffer.extend(to_add)
            hashset = hashset | set([nd.val for nd in to_add])
            if target in hashset:
                ret = level + 1
                break
            if p0 == p1:
                p1 = len(buffer) - 1
                level += 1
            p0 += 1
        return ret

def word_graph_distance(
                        begin_word: str,
                        end_word: str,
                        word_list: List[str],
                        ) -> int:
    graph = Graph()
    for word in word_list:
        graph.add(Node(word))
    if end_word not in graph.nodes:
        ret = 0
    elif begin_word == end_word:
        ret = 0
    else:
        ret = graph.get_distance(begin_word, end_word)
    return ret

def test():
    begin_word = "hot"
    end_word = "dog"
    word_list = ["hot", "dog", "dot"]
    print(word_graph_distance(begin_word, end_word, word_list))

if __name__=="__main__":
    test()



