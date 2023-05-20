#Name: Nick Bear
#Date: 5/20/2023
#Assignment: Add Two Numbers

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class AddTwoNumbers:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        #initialize values needed for object
        #carry is used to keep track of carries over to the next place
        ans = ListNode()
        curr = ans
        carry = 0
        
        #while there are still digits
        while (l1 or l2 or carry):
            
        #v is the value of the listnode if it exists or its 0
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0
        
        #the value of the next listnode is the addition of v1, v2, and the carry
            val = v1 + v2 + carry
            
        #the new carry is the integer division of value
            carry = val // 10
            
        #the new value is value modulo 10
            val = val % 10
            curr.next = ListNode(val)
            
            #update pointers
            curr = curr.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
                    
        #return list of added values
        return ans.next
