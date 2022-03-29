# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        def inOrder(root, nodes):
            if root:
                inOrder(root.left, nodes)
                nodes.append(root.val)
                inOrder(root.right, nodes)
        res = []
        if root:
            inOrder(root, res)
        return res[k-1]