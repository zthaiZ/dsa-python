import math

def smallest_subarray_sum(s, arr):
  minLen = math.inf
  winSum = 0
  l = 0

  for r in range(len(arr)):
    winSum += arr[r]

    while (winSum >= s):
      minLen = min(minLen, r - l + 1)
      winSum -= arr[l]
      l += 1

  if minLen == math.inf:
    return 0

  return minLen

