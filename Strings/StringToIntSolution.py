#Name: Nicholas Bear
#Date: 5/14/23
#Assignment: String to Integer (atoi)

class StringToIntSolution:
    def myAtoi(self, s: str) -> int:
        
        parsed = 0
        
        #remove whitespace
        s = s.lstrip()
        
        #if s is empty, return 0
        if not s:
            return 0
        
        #index for parsing string
        i = 0
        
        #hold sign of integer
        sign = 1
        
        #change sign depending on operator encountered at the beginning of the string
        if s[i] == "-":
            i+=1
            sign = -1
            
        elif s[i] == "+":
            i+=1
            
        #while i is in the bounds of the length of the string
        while (i < len(s)):
            
            curr = s[i]
            
            #if the curr index of s is not a digit, break the loop
            if (not curr.isdigit()):
                break
                
            #else parse the string
            else:
                parsed = parsed*10 + int(curr)
            
            #keep incrementing our index
            i+=1

        #use the sign stored    
        parsed *=sign

        #check edge cases, else return parsed
        if (parsed > 2**31 - 1):
            return 2**31 - 1

        elif (parsed <= 2**31 * -1):
            return 2**31 * -1

        else:
            return parsed
