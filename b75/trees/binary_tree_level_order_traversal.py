from collections import deque

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return None
    
        queue = deque()
        queue.append(root)
        res = []
        
        while(queue):
            levelSize = len(queue)
            levelValues = []
            for node in range(levelSize):
                currNode = queue.popleft()
                
                levelValues.append(currNode.val)
                
                if currNode.left:
                    queue.append(currNode.left)
                if currNode.right:
                    queue.append(currNode.right)
                    
            res.append(levelValues)
            
        return res