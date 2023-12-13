#q: given an Linked List , Determine or Check if it has cycle or not 


#Definition for singly-linked list

class ListNode(object):
  def __init__(self,x):
    self.val = x
    self.next = None


class Solution(object):
  def hasCycle(self,head):
    """
    :type head: ListNode
    :rtype : bool

    """
    if head == None:
      return False
    else:
      fast = head
      slow = head

      while fast != None and fast.next != None:
        slow = slow.next
        fast = fast.next.next
        if fast == slow:
          break

      if fast == None or fast.next == None:
        return False
      elif fast == slow:
        return True  
      

      return False




#cheaking the Functions


# Creating a linked list with a cycle
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
head.next.next.next.next = ListNode(5)
head.next.next.next.next.next = head.next  # creating a cycle

# Using the solution to check for a cycle
solution = Solution()
result = solution.hasCycle(head)

# Printing the result
print(result)  # Output: True      