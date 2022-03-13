from typing import List, Optional
import collections

class Node():
    def __init__(self, val: Optional[bool]):
        """
        left = false / 0
        right = true / 1
        could save memory?
        """
        self.val = val
        self.children = dict()

class Trie():
    def __init__(self, max_power: int):
        self.root = Node(None)
        self.max_power = max_power

    def add(self, num: int):
        node = self.root
        counter = 0
        for counter in range(self.max_power + 1):
            bit = (num >> (self.max_power - counter)) & 1
            if bit in node.children:
                pass
            else:
                node.children[bit] = Node(bit)
            node = node.children[bit]
        if num not in node.children:
            node.children[True] = Node(num)

    def find_max_xor_for_number(self, num: int) -> int:
        mp = self.max_power
        node = self.root
        for counter in range(mp + 1):
            comp_bit = 1 - (num >> (mp - counter) & 1)
            if comp_bit in node.children:
                node = node.children[comp_bit]
            else:
                node = node.children[1 - comp_bit]
        return (node.children[True].val ^ num)

def find_max_xor(nums: List[int]) -> int:
    max_power = 32
    trie = Trie(max_power)
    for num in nums:
        trie.add(num)
    max_xor = 0
    for num in nums:
        val = trie.find_max_xor_for_number(num)
        max_xor = val if val > max_xor else max_xor
    return max_xor

def test():
    import numpy as np
    nums = np.random.randint(0, 2**9 - 1, 100)
    print(nums)
    print(find_max_xor(nums))

if __name__=="__main__":
    test()

