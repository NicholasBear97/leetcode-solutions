#Name: Nick Bear
#Date: 5/16/2023
#Assignment: Longest Substring Without Repeating Characters

class LongestSS:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        #initialize variables for tracking
        seen = set()
        l = 0
        result = 0
        
        #right pointer will start at the end of our for loop
        for r in range(len(s)):
            
            #if the right pointer points to a char in the set, remove the left pointer's char and update where the left pointer points
            while(s[r] in seen):
                seen.remove(s[l])
                l += 1
                
            #add right pointer char to the set    
            seen.add(s[r])
            
            #return the max of result recorded vs current window size
            result = max(result, r - l + 1)
        return result
