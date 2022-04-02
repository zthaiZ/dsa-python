def pair_with_targetsum(arr, target_sum):
  l = 0
  prev = {}
  #X + Y = Target ---> X = Target - Y
  for r in range(len(arr)):
    diff = target_sum - arr[r]
    if diff in prev:
      return [prev[diff], r]

    prev[arr[r]] = r

  return [-1, -1]
