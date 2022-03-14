from typing import List, Type, Optional

class TreeNode():
    def __init__(self, val: int, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def call_step(node: TreeNode):
    lf = (call_step(node.left) if (node.left is not None)
          else (float("-inf"), float("-inf")))
    rt = (call_step(node.right) if (node.right is not None)
          else (float("-inf"), float("-inf")))
    single_sum = max(
                    node.val,
                    node.val + lf[0],
                    node.val + rt[0],)
    two_branch_sum = max(
                    node.val + lf[0] + rt[0],
                    lf[1],
                    rt[1],
                    lf[0],
                    rt[0],
                    )
    ret = (single_sum, two_branch_sum)
    return ret

def maximum_path_sum(head: Optional[TreeNode]):
    if head is not None:
        single_sum, two_branch_sum = call_step(head)
        ret = max(single_sum, two_branch_sum)
    else:
        ret = 0
    return ret
