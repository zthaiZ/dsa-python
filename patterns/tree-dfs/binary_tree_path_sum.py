class TreeNode:
  def __init__(self, val, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right


def has_path(root, sum):
  stack = []
  if not root:
    return False

  stack.append((root, root.val))

  while stack:
    pathSum = 0
  
    for i in range(len(stack)):
      node, val = stack.pop()

      if not node.right and not node.left and val == sum:
        return True

      if node.left:
        stack.append((node.left, val+node.left.val))

      if node.right:
        stack.append((node.right, val+node.right.val))

  return False

def main():

  root = TreeNode(12)
  root.left = TreeNode(7)
  root.right = TreeNode(1)
  root.left.left = TreeNode(9)
  root.right.left = TreeNode(10)
  root.right.right = TreeNode(5)
  print("Tree has path: " + str(has_path(root, 23)))
  print("Tree has path: " + str(has_path(root, 16)))


main()
