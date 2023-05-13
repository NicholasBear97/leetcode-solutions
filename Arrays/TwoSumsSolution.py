#Name: Nick Bear
#Date: 5/13/23
#Assignment: Two Sums
class TwoSumsSolution.py:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        #hashmap to store values previously visited by index, value
        prevMap = {}
        
        #for each element in nums, the difference is the target minus that element's value
        for i, n in enumerate(nums):
            
            diff = target - n
            
            #if the diff exists within the hashmap prevMap, return the index of that diff and the current index
            if diff in prevMap:
                return [prevMap[diff], i]
            
            #else, store n at the current index into the hashmap
            prevMap[n] = i
