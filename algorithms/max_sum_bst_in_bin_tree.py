"""
Given a binary tree, find the maximum node sum among
    all BST subtrees
"""

class TreeNode():
    def __init__(self, val,
                 left: Optional[TreeNode]=None,
                 right: Optional[TreeNode]=None):
        self.val = val
        self.left = left
        self.right = right

def assign_is_bst(root: TreeNode) -> Tuple[bool, float, float]:
    if root.left is not None:
        lf_is_bst, lf_lb, lf_ub = assign_is_bst(root.left)
    else:
        lf_is_bst =(True, float("inf"), float("-inf"))
    if root.right is not None:
        rt_is_bst, rt_lb, rt_ub = assign_is_bst(root.right)
    else:
        rt_is_bst =(True, float("inf"), float("-inf"))
    if ((lf_is_bst and rt_is_bst)
            and (root.val >= lf_ub)
            and (root.val <= rt_lb)):
        is_bst = True
    else:
        is_bst = False
    lb = min(lf_lb, root.val)
    ub = max(rt_ub, root.val)
    root.is_bst = is_bst
    ret = (is_bst, lb, ub)
    return ret

def assign_sum(root: TreeNode) -> float:
    ret = root.val
    if root.left is not None:
        ret += assign_sum(root.left)
    if root.right is not None:
        ret += assign_sum(root.right)
    root.sum = ret
    return ret

def get_max(root: TreeNode, maxval: float) -> float:
    if root.is_bst:
        maxval = max(maxval, root.sum)
    if root.left is not None:
        maxval = max(maxval, get_max(root.left, maxval))
    if root.right is not None:
        maxval = max(maxval, get_max(root.right, maxval))
    return maxval

def find_max_bst_sum(root: TreeNode) -> float:
    if root is not None:
        assign_is_bst(root)
        assign_sum(root)
        ret = get_max(root, float("-inf"))
    else:
        ret = float("-inf")
    return ret
