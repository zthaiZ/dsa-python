def triplet_with_smaller_sum(arr, target):
  count = 0
  arr.sort()

  for i in range(len(arr)):
    l,r = i+1,len(arr) - 1

    while l < r:
      curSum = arr[i] + arr[l] + arr[r]
      if curSum < target:
        count += r-l #then all other numbers between l and r are also smaller

        l += 1
      else:
        r -= 1

  return count
