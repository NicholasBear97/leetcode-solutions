#Name: Nick Bear
#Date: 5/21/23
#Assignment: 1480. Running Sum of 1d Array

class RunningSumSltn:
    def runningSum(self, nums: List[int]) -> List[int]:

        #start with temp value = 0
        ans = 0

        #have i keep track of index and n keep track of value to be added to temp
        for i, n in enumerate(nums):
        
        #temp value keeps accumulating for the next index assignment
            ans += n
            nums[i] = ans

        return nums
