#Name: Nick Bear
#Date: 1/24/2023
#Assignment: Leetcode 27 Remove Element
class RemoveElement:
    def removeElement(self, nums: List[int], val: int) -> int:
      
        #create left pointer to keep track of all elements that do not equal the target value
        l = 0

        #iterate through nums to find the target value
        #if the current element being accessed does not equal the target value
        #set the address of the last index recorded by the left pointer equal to the element
        for r in nums:
            if r != val:
                nums[l] = r
                l+=1
                
        #return the number of elements not equal to the target value
        return l
