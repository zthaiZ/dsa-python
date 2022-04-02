def search_triplets(arr):
  triplets = []

  #X + Y + Z = 0 --> Y + Z = -X 
  # sort array first, then we can shift pointers depending on if they are > or < 0
  arr.sort()

  for i in range(len(arr)):
    if i>0 and arr[i] == arr[i-1]:
      continue

    l,r = i+1, len(arr) - 1
    while l < r:
      threeSum = arr[i] + arr[l] + arr[r]

      if threeSum == 0:
        triplets.append([arr[i], arr[l], arr[r]])
        l+=1

        while l < r and arr[l] == arr[l-1]:
          l+=1

      elif threeSum < 0:
        l += 1

      else:
        r -= 1

  
  return triplets
