# Given an array of positive numbers and a positive number âk,â find the maximum sum of any contiguous subarray of size âkâ

def max_sub_array_of_size_k(arr, k):
  start = 0
  window_sum = 0
  max_sum = 
  
  for end in range(len(arr)):
    window_sum += arr[end]
    
    if end >= k-1:
      max_sum = max(max_sum, window_sum)
      window_sum -= arr[start]
      start += 1

  return max_sum

def main():
  print(max_sub_array_of_size_k([2, 1, 5, 1, 3, 2], 3))

main()
  