#Name: Nick Bear
#Date: 2/3/2023
#Assignment: Leetcode 206 Reverse Linked List

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class ReverseLinkedList:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        #create two pointers, prev and curr.
        #prev points at None or NULL because there are no nodes before the head at the start of the program
        #curr represents the current node being accessed which is head at the start of the program
        prev = None
        curr = head

        #create a while loop that will go through each node until the end of the list
        #we have reached the end of the list when the curr node we are accessing is None or NULL due to the initial tail pointer pointing towards None or NULL
        while curr:

            #create a next pointer that holds the current next pointer at the beginning of the iteration
            next = curr.next

            #now change the current next pointer to the prev pointer
            curr.next = prev

            #update the prev pointer to the current node
            prev = curr

            #finally set the curr node equal to next which stores the next pointer we previously had
            curr = next

        #return the new head which is held in the prev pointer variable
        return prev
