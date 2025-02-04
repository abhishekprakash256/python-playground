from linked_list import LinkedList

def detect_cycle(head):

   # Replace this placeholder return statement with your code

   if head is None:
      return False

   slow = head
   fast = head

   while fast and fast.next:

      slow = slow.next
      fast = fast.next.next

      if slow == fast:

         return True


   return False