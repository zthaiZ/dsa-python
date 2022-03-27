from collections import deque


class TreeNode:
  def __init__(self, val):
    self.val = val
    self.left, self.right = None, None


def traverse(root):
  result = []
  if root is None:
    return result

  queue = deque()
  queue.append(root)
  leftToRight = True

  while(queue):
    lvlsize = len(queue)
    lvlres = deque()
    for node in range(lvlsize):
      currNode = queue.popleft()

      if leftToRight:
        lvlres.append(currNode.val)
      else:
        lvlres.appendleft(currNode.val)

      if currNode.left:
        queue.append(currNode.left)
      if currNode.right:
        queue.append(currNode.right)

    leftToRight = not leftToRight
    result.append(list(lvlres))    

  return result


def main():
  root = TreeNode(12)
  root.left = TreeNode(7)
  root.right = TreeNode(1)
  root.left.left = TreeNode(9)
  root.right.left = TreeNode(10)
  root.right.right = TreeNode(5)
  root.right.left.left = TreeNode(20)
  root.right.left.right = TreeNode(17)
  print("Zigzag traversal: " + str(traverse(root)))


main()
