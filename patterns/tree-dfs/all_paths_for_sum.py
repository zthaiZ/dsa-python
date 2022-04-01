class TreeNode:
  def __init__(self, val, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right


def find_paths(root, s):
  allPaths = []

  if not root:
    return None

  stack = [(root, [root.val])]

  while stack:
    for i in range(len(stack)):
      node, vals = stack.pop()

      if not node.left and not node.right and sum(vals) == s:
        allPaths.append(vals)

      if node.left:
        stack.append((node.left, vals+[node.left.val]))

      if node.right:
        stack.append((node.right, vals+[node.right.val]))

  return allPaths


def main():

  root = TreeNode(12)
  root.left = TreeNode(7)
  root.right = TreeNode(1)
  root.left.left = TreeNode(4)
  root.right.left = TreeNode(10)
  root.right.right = TreeNode(5)
  sum = 23
  print("Tree paths with sum " + str(sum) +
        ": " + str(find_paths(root, sum)))


main()
