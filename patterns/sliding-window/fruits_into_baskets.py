# You are visiting a farm to collect fruits. The farm has a single row of fruit trees. You will be given two baskets, and your goal is to pick as many fruits as possible to be placed in the given baskets.

# You will be given an array of characters where each character represents a fruit tree. The farm has following restrictions:

# Each basket can have only one type of fruit. There is no limit to how many fruit a basket can hold.
# You can start with any tree, but you can’t skip a tree once you have started.
# You will pick exactly one fruit from every tree until you cannot, i.e., you will stop when you have to pick from a third fruit type.
# Write a function to return the maximum number of fruits in both baskets.

# Example 1:

# Input: Fruit=['A', 'B', 'C', 'A', 'C']
# Output: 3
# Explanation: We can put 2 'C' in one basket and one 'A' in the other from the subarray ['C', 'A', 'C']

def fruits_into_baskets(fruits):
  #max number of fruits - track # of chars that satisfy constraint of two baskets
  #using a dict/hashmap will help for tracking # of occurances

  collected = {}
  start = 0
  max_fruit = 0
  baskets = 2

  for end in range(len(fruits)):
    if fruits[end] not in collected:
      collected[fruits[end]] = 0
    collected[fruits[end]] += 1

    while (len(collected) > baskets):
      collected[fruits[start]] -= 1
      if collected[fruits[start]] == 0:
        del collected[fruits[start]]
      start += 1

    max_fruit = max(max_fruit, end - start + 1)

  return max_fruit
