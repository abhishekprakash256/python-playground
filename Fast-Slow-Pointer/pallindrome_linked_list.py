"""
To check the pallindrome of the linked list 
Given the head of a linked list, your task is to check whether the linked list is a palindrome or not. 
Return TRUE if the linked list is a palindrome; otherwise, return FALSE.

"""

#-------------------------------------the file that helps to rotate the linked list ----------------------------

from linked_list_node import * 
from linked_list import *


#make the linked list 

head = LinkedListNode(1)
node2 = LinkedListNode(2)
node3 = LinkedListNode(2)
node4 = LinkedListNode(1)
node5 = LinkedListNode(5)

#connect the linked list 
head.next = node2
node2.next = node3
node3.next = node4
node4.next = node5


#print list 

class LinkedList_helper(LinkedList):

    def linked_lst_print(self,node):

        temp = node

        while True:

            print(temp.data)
            if temp.next is None:
                break
            
            temp = temp.next

    def reverse_lst(self,node):

        prev , curr = None, node

        while curr:

            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt

        return prev
        
            



if __name__ == "__main__":
    helper = LinkedList_helper()

    helper.linked_lst_print(head)

    helper.reverse_lst(head)

    helper.linked_lst_print(head)



