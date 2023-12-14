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
#head.next.next.next.next.next.next = None  try this will give false ans

# Using the solution to check for a cycle
solution = Solution()
result = solution.hasCycle(head)

# Printing the result
print(result)  # Output: True      



# Explanation: 
#The problem is about determining whether a given linked list contains a cycle or not. 
# A cycle in a linked list occurs when there is a node in the list whose "next" pointer
# points to a node that appears earlier in the list, creating a loop.

# The provided solution uses the Floyd's cycle-finding algorithm, also known as the 
# "tortoise and hare" algorithm. It employs two pointers, one moving at twice the speed of the other. 
# If there is a cycle, the faster pointer will eventually catch up with the slower one,
#  indicating the presence of a cycle.

# Here's how the algorithm works in the provided code:

# Initialize two pointers, slow and fast, both pointing to the head of the linked list.
# Move slow one step at a time and fast two steps at a time.
# If there is a cycle, the fast pointer will eventually catch up with the slow pointer.
# If there is no cycle, the fast pointer will reach the end of the list (i.e., None).
# The code checks for the existence of a cycle by monitoring the positions of the slow and
#   fast pointers. If a cycle is found, the loop is terminated early, and the function returns True.
# If the fast pointer reaches the end of the list without encountering a cycle, the function returns False.