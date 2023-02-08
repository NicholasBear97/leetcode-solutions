#Name: Nick Bear
#Date: 2/8/2023
#Assignment: Leetcode 21 Merge Two Sorted Lists

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class MergeSolution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        #Create a null dummy node to begin the linkedlist solution
        dummy = ListNode()

        #Create a tail pointer = dummy node
        tail = dummy

        #Compare each list value while both exists
        while (list1 and list2):

            #If list1 value is greater than list2 value, set the next pointer of tail equal to list2
            #Update the list2 pointer
            if list1.val >= list2.val:
                tail.next = list2
                list2 = list2.next

            #Else set the next pointer of tail equal to list1
            #Update the list1 pointer
            else:
                tail.next = list1
                list1 = list1.next

        #Update your tail pointer to the current merged node
            tail = tail.next
            
        #Once one or more lists do not exists, check for any remaining nodes in both
        #If any nodes remain, append them to the end of the merged list

        #list1 still exists
        if (list1):
            tail.next = list1

        #list2 still exists    
        elif (list2):
            tail.next = list2

        #Return dummy.next which holds the head of your merged list
        return dummy.next  
