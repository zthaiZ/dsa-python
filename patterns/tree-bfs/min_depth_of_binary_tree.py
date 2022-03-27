from collections import deque

class TreeNode:
  def __init__(self, val):
    self.val = val
    self.left, self.right = None, None


def find_minimum_depth(root):

  if root is None:
    return 0

  queue = deque()
  queue.append(root)
  min_depth = 0

  while(queue):
    min_depth +=1 

    for node in range(len(queue)):
      currNode = queue.popleft()

      if not currNode.left and not currNode.right:
        return min_depth

      if currNode.left:
        queue.append(currNode.left)
      if currNode.right:
        queue.append(currNode.right)

  return min_depth


def main():
  root = TreeNode(12)
  root.left = TreeNode(7)
  root.right = TreeNode(1)
  root.right.left = TreeNode(10)
  root.right.right = TreeNode(5)
  print("Tree Minimum Depth: " + str(find_minimum_depth(root)))
  root.left.left = TreeNode(9)
  root.right.left.left = TreeNode(11)
  print("Tree Minimum Depth: " + str(find_minimum_depth(root)))


main()
