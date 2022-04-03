from __future__ import print_function


class Node:
  def __init__(self, value, next=None):
    self.value = value
    self.next = next

  def print_list(self):
    temp = self
    while temp is not None:
      print(temp.value, end='')
      temp = temp.next
    print()


def find_cycle_start(head):
  slow = head
  fast = head
  cycle_length = 0
  while(fast is not None and fast.next is not None):
    slow = slow.next
    fast = fast.next.next

    if slow == fast:
      current = slow
      counter = 0
      while (True):
        current = current.next
        counter+=1
        if current == slow:
          cycle_length = counter
          break

  pt1 = head
  pt2 = head

  while(cycle_length > 0):
    pt1 = pt1.next
    cycle_length -= 1

  while(pt1 != pt2):
    pt1 = pt1.next
    pt2 = pt2.next

  return pt1


def main():
  head = Node(1)
  head.next = Node(2)
  head.next.next = Node(3)
  head.next.next.next = Node(4)
  head.next.next.next.next = Node(5)
  head.next.next.next.next.next = Node(6)

  head.next.next.next.next.next.next = head.next.next
  print("LinkedList cycle start: " + str(find_cycle_start(head).value))

  head.next.next.next.next.next.next = head.next.next.next
  print("LinkedList cycle start: " + str(find_cycle_start(head).value))

  head.next.next.next.next.next.next = head
  print("LinkedList cycle start: " + str(find_cycle_start(head).value))


main()
