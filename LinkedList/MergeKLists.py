#Name: Nick Bear
#Date: 5/21/2023
#Assignment: Merge K Sorted Lists

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class MergeKLists:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:

        #if the list is empty, return null
        if not lists or len(lists) == 0:
            return None

        #while there are k lists where k > 1
        while len(lists) > 1:

        #create an empty temp variable
            mergedList = []

        #for every other list in lists, merge it and its neighbor and then add it to the temp variable
            for i in range(0, len(lists), 2):
                l1 = lists[i]
                l2 = lists[i + 1] if i+1 < len(lists) else None
                mergedList.append(self.mergeList(l1, l2))
        
        #update lists variable to hold newly sorted lists cut in half
            lists = mergedList

        return lists[0]

    
    #LeetCode Easy Merge List function
    def mergeList(self, l1, l2):
        ans = ListNode()
        curr = ans

        while(l1 and l2):
            if (l1.val > l2.val):
                curr.next = l2
                l2 = l2.next
            else:
                curr.next = l1
                l1 = l1.next

            curr = curr.next
        
        if(l1):
            curr.next = l1
        
        if(l2):
            curr.next = l2
        
        return ans.next
