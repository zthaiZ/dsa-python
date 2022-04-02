import math

def triplet_sum_close_to_target(arr, target_sum):
  # Given an array of unsorted numbers and a target number, find a triplet in the array whose sum is as close to the target number as possible, return the sum of the triplet. If there are more than one such triplet, return the sum of the triplet with the smallest sum.
  #
  arr.sort()

  minDiff = math.inf
  closeSum = 0
  for i in range(len(arr)):

      l = i + 1
      r = len(arr) - 1
      while l < r:
        currSum = arr[i] + arr[l] + arr[r]
        diff = abs(currSum - target_sum)
        if diff < minDiff:
          closeSum = currSum
          minDiff = diff

        if target_sum == currSum:
          return target_sum

        elif target_sum > currSum:
          l += 1
        else:
          r -= 1

  return closeSum
    


        



  return -1
