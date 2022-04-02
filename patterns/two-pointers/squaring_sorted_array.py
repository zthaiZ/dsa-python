def make_squares(arr):
  squares = []
  left = 0
  right = len(arr) -1
  while (left <= right):
    leftSquare = arr[left] * arr[left]
    rightSquare = arr[right] * arr[right]

    if leftSquare < rightSquare:
      squares.append(leftSquare)
      squares.append(rightSquare)
    else:
      squares.append(rightSquare)
      squares.append(leftSquare)
    left += 1
    right -= 1
  return squares
