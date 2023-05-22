#Name: Nick Bear
#Date: 5/22/23
#Assignment: 876. Middle of the Linked List

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class MiddleNode:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        #two pointer problem
        tail, middle = head, head

        #tail traverses twice an iteration while middle traverses once in an iteration
        while tail:
            tail = tail.next

            #if tail is not null, we have more nodes to visit, else we reached the end of the list
            if tail:
                tail = tail.next
            else:
                break

            middle = middle.next
        
        return middle
