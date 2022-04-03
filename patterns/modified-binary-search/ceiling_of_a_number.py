def search_ceiling_of_a_number(arr, key):
  l = 0
  r = len(arr) - 1

  if arr[r] < key:
    return -1

  while l < r:

    mid = l + (r-l) // 2

    if arr[mid] < key:
      l = mid + 1
    elif arr[mid] > key:
      r = mid - 1

    else:
      return mid

  return l


def main():
  print(search_ceiling_of_a_number([4, 6, 10], 6))
  print(search_ceiling_of_a_number([1, 3, 8, 10, 15], 12))
  print(search_ceiling_of_a_number([4, 6, 10], 17))
  print(search_ceiling_of_a_number([4, 6, 10], -1))


main()
