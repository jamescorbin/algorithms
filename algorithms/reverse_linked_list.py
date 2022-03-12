from typing import Optional, Type

class Node:
    def __init__(self, val: int, nxt: Optional[Type[Node]]):
        self.val = val
        self.next = nxt

def flip(node: Optional[Node]) -> Optional[Node]:
    if (node is not None) and (node.next is not None):
        flip(node.next).next = node
    return node

def reverse_linked_list(head: Optional[Node]):
    tail = head
    while (tail is not None) and (tail.next is not None):
        tail = tail.next
    flip(head)
    if head is not None:
        head.next = None
    return tail
