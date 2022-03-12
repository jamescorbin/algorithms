from typing import Optional, List, Type

class TreeNode():
    def __init__(self,
                 val: int,
                 left: Optional[Type[TreeNode]]=None,
                 right: Optional[Type[TreeNode]]=None,):
        self.val = val
        self.left = left
        self.right = right

def get_inorder(head: Optional[TreeNode], vals: List[int]) -> None:
    if head is not None:
        if head.left is not None:
            get_inorder(head.left, vals)
        vals.append(head.val)
        if head.right is not None:
            get_inorder(head.right, vals)

def build_bst(vals: List[int]) -> TreeNode:
    m = len(vals)
    if m > 0:
        head = TreeNode(vals[m // 2])
        head.left = build_bst(vals[:m // 2])
        head.right = build_bst(vals[m // 2 + 1:])
    else:
        head = None
    return head

def balance_bst(head: Optional[TreeNode]) -> Optional[TreeNode]:
    vals = []
    get_inorder(head, vals)
    return build_bst(vals)

