def remove_duplicates(arr):
  l = 0 #next non dup
  r = 0
  seen = set()
  while l<=r and r < len(arr):
    print(arr)
    print(l)
    if arr[r] not in seen:
      print('found not dup '+str(arr[r]))
      seen.add(arr[r])
      arr[l] = arr[r]
      l += 1
    r+=1
  return l
