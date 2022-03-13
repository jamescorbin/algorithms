from typing import List, Tuple, Dict, Set
import collections

class Node():
    def __init__(self, val: str, idx: Tuple[int, int]):
        self.val = val
        self.idx = idx
        self.adj = dict()

class Board():
    def __init__(self):
        self.nodes = collections.defaultdict(list)

    def add(self, node: Node) -> None:
        self.nodes[node.val].append(node)

    def search(self, word: str, ignore: Set[Tuple[int, int]]) -> bool:
        ret = False
        if len(word) == 0:
            ret = True
        else:
            if word[0] in self.nodes:
                next_nodes = [nd for nd in self.nodes[word[0]]
                              if nd.idx not in ignore]
                for nd in next_nodes:
                    new_ignore = set(ignore | set([nd.idx]))
                    ret = ret | self.search(word[1:], new_ignore)
        return ret

def find_word_in_board(board: List[List[str]], word: str) -> bool:
    boardo = Board()
    for i in range(len(board)):
        lst = board[i]
        for j in range(len(lst)):
            nd = Node(lst[j], (i, j))
            boardo.add(nd)
    return boardo.search(word, set())

def test():
    arr = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
    word = "ABCCED"
    print(find_word_in_board(arr, word))

if __name__=="__main__":
    test()
