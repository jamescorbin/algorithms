"""
You are given the root of a binary search tree (BST), where the values of exactly two nodes of the tree were swapped by mistake. Recover the tree without changing its structure.
"""
from typing import Optional, Tuple

def _get_swaps(node: "Node", 
                   prev_node: Optional["Node"]=None, 
                   left_bad: Optional["Node"]=None,
                   right_bad: Optional["Node"]=None,
                   ) -> Tuple["Node", bool]:
    if (node.left is not None):
        prev_node, left_bad, right_bad = _get_swaps(
                node.left, 
                prev_node, 
                left_bad, 
                right_bad)
    if (prev_node is not None) and (node.val < prev_node.val):
        if left_bad is None:
            left_bad = prev_node
        right_bad = node
    prev_node = node
    if node.right is not None:
        prev_node, left_bad, right_bad = _get_swaps(
                node.right, 
                prev_node, 
                left_bad, 
                right_bad)
    return prev_node, left_bad, right_bad
    
def _swap(node: "Node") -> None:
    """
    Morris Traversal: traverse tree in order without stack or 
        recurrsion
    """
    curr, prev, left_bad, right_bad = node, None, None, None
    while curr:
        # next four lines are additions to Morris Traversal
        if (prev is not None) and curr.val < prev.val:
            if left_bad is None:
                left_bad = prev
            right_bad = curr          
        if curr.left is None:  
            prev = curr
            curr = curr.right                
        else:
            temp = curr.left
            while temp.right and temp.right is not curr:
                temp = temp.right
            if temp.right is curr:
                temp.right = None             
                prev = curr
                curr = curr.right
            else:
                temp.right = curr
                curr = curr.left
    left_bad.val, right_bad.val = right_bad.val, left_bad.val

class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if root is not None:
            a, nd1, nd2 = _get_swaps(root)
            nd1.val, nd2.val = nd2.val, nd1.val
