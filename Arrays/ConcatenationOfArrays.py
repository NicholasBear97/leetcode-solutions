#Name: Nick Bear
#Date: 1/25/2023
#Assignment: Leetcode 1929 Concatenation of Array
class ConcatenationOfArrays:
    def getConcatenation(self, nums: List[int]) -> List[int]:
      
      #Create a variable answer that holds the addition of the passed array
      #Because lists are dynamic arrays, we can simply add them together
        ans = nums+nums
        
        #Return the answer variable
        return ans
