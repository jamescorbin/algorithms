from typing import Optional

class Node():
    def __init__(self,
                 val: int,
                 next: Optional[object]=None,
                 random: Optional[object]=None):
        self.val = val
        self.next = None
        self.random = None

def get_list_length(head: Optional[Node]) -> int:
    count = 0
    while head is not None:
        head = head.next
        count += 1
    return count

def go_to_k(head: Optional[Node], k: int) -> Optional[Node]:
    while (k > 0) and head is not None:
        head = head.next
        k -= 1
    return head

class Solution:
    def copyRandomList(self, head: Optional[Node]) -> Optional[Node]:
        """
        O(1) space, O(n2) time solution
        """"
        n = get_list_length(head)
        p = head
        new_head = None
        q = None
        while p is not None:
            nd = Node(p.val)
            if new_head is None:
                new_head = nd
                q = new_head
            else:
                q.next = nd
                q = nd
            p = p.next
        p = head
        i = 0
        while p is not None:
            q = p.random
            k = (n - get_list_length(q))
            if k < n:
                go_to_k(new_head, i).random = go_to_k(new_head, k)
            p = p.next
            i += 1
        return new_head

    def copyRandomListQuick(self, head: Optional[Node]) -> Optional[Node]:
        """
        O(n) space, O(n) time
        """
        ids = {}
        rand_ids = []
        p = head
        counter = 0
        while p is not None:
            ids[id(p)] = counter
            rand_ids.append(id(p.random) if p.random else None)
            counter += 1
            p = p.next
        nd_lst = []
        p = head
        counter = 0
        while p is not None:
            nd = Node(p.val)
            nd_lst.append(nd)
            p = p.next
            if counter > 0:
                nd_lst[counter - 1].next = nd_lst[counter]
            counter += 1
        for i, nd in enumerate(nd_lst):
            rand_id = rand_ids[i]
            if rand_id:
                idx = ids[rand_id]
                nd_lst[i].random = nd_lst[idx]
        ret = nd_lst[0] if len(nd_lst) > 0 else None
        return ret

    def copyRandomListOptimal(self, head: Optional[Node]) -> Optional[Node]:
        """
        O(1) space, O(n) time;
        Zigzag / alternating algorithm
        """
        p = head
        while p is not None:
            nd = Node(p.val)
            nd.next = p.next
            p.next = nd
            p = p.next.next
        p = head
        while p is not None:
            if p.random is not None:
                p.next.random = p.random.next
            p = p.next.next
        p = head
        q = p.next if p is not None else None
        new_head = q
        while p is not None:
            nd0 = p
            p = p.next.next
            nd0.next = p
            nd1 = q
            if q.next is not None:
                q = q.next.next
                nd1.next = q
            else:
                nd1.next = None
                q = None
        return new_head

