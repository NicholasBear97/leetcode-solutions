#Name: Nick Bear
#Date: 1/31/2023
#Assignment: Leetcode 20 Valid Parentheses
class IsValidSolution:
    def isValid(self, s: str) -> bool:

        #create empty stack to keep track of order of parentheses
        stack = []

        #create HashMap to keep track of matching parentheses 
        parentheses = { ")" : "(", "}" : "{", "]" : "[" }

        #iterate through every index of string s
        for p in s:

            #if p is a closing parentheses, make sure the stack holding open parentheses isn't empty AND the current closing parentheses (p) matches last open parentheses (top of stack or stack[-1])
            if p in parentheses:
                if stack and stack[-1] == parentheses[p]:

                    #pop the open parentheses from stack if it matches
                    stack.pop()

                #else return false becaues they do not match and the brackets are not in the correct order
                else: 
                    return False

            #else p is an open parentheses so we must add it to the stack
            else:
                stack.append(p)
        #return true if the stack is completely empty (all parentheses have been matched and popped)        
        return True if not stack else False
