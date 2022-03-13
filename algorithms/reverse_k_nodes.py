from typing import Optional, Type

class ListNode():
    def __init__(self, val: int, nxt: Optional[None]=None):
        self.val = val
        self.next = nxt

def reverse_k_group(node: ListNode, k: int, start: bool = True) -> ListNode:
    if (k > 1) and (node is not None):
        reverse_k_group(node.next, k - 1, False).next = node
    if start:
        node.next = None
    return node

def advance_k(node: ListNode, k: int) -> ListNode:
    while (node is not None) and (k > 0):
        node = node.next
        k -= 1
    return node

def reverse_nodes_k_group(head: Optional[ListNode],
                          k: int) -> Optional[ListNode]:
    dummy = ListNode(0)
    dummy.next = head
    prenode = dummy
    while (prenode is not None) and (k > 1):
        startnode = prenode.next
        tailnode = advance_k(startnode, k - 1)
        if tailnode is not None:
            postnode = advance_k(tailnode, 1)
            reverse_k_group(startnode, k)
            prenode.next = tailnode
            startnode.next = postnode
            prenode = startnode
        else:
            prenode = tailnode
    return dummy.next

def test():
    head = ListNode(1,
                    nxt=ListNode(2,
                    nxt=ListNode(3,
                    nxt=ListNode(4,
                    nxt=ListNode(5)))))
    reverse_nodes_k_group(head, 2)

if __name__=="__main__":
    test()

