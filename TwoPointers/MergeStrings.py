#Name: Nick Bear
#Date: 5/13/2023
#Assignment: Leetcode 1768. Merge Strings Alternately

class MergeStrings:
    def mergeAlternately(self, word1: str, word2: str) -> str:
      
        #create two pointers and an empty arr to hold the string characters
        i, j = 0, 0

        res = []
        
        #while both pointers stay within the bounds of word1 and word2, add their characters at each pointer index to the arr res
        while (i < len(word1) and j < len(word2)):
            res.append(word1[i])
            i+=1
            res.append(word2[j])
            j+=1

        #add remaining characters to the arr res
        res.append(word1[i:])
        res.append(word2[j:])

        #return the arr joined together by the "" delimiter
        return "".join(res)
