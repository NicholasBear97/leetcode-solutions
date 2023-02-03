#Name: Nick Bear
#Date: 1/23/2023
#Assignment: Leetcode 26 Remove Duplicates from Sorted Array

class RemoveDuplicates:
    def removeDuplicates(self, nums: List[int]) -> int:
      
        #create a left pointer to tell us where to store the next unique element
        l = 1

        #iterate though the passed array, nums
        #the right pointer starts at 1 because we are evaluating the element at the current index in nums versus the element at the previous index in nums
        #e.g: nums[1] vs nums[0]; nums[2] vs nums[1]; ...; nums[len(nums)] vs nums[len(nums)-1];
        for r in range(1, len(nums)):

            #if the current element being accessed doesn't equal the previous element, it is unique
            #set the address of the last index recorded by the left pointer equal to the current element
            if nums[r] != nums[r-1]:
                nums[l] = nums[r]

                #increase the left pointer to keep track of where to place the next non repeating element AND count how many unique elements nums has
                l+=1
                
        #return the left pointer to return the number of unique elements in nums       
        return l
