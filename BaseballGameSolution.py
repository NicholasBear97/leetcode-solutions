#Name: Nick Bear
#Date: 1/29/2023
#Assignment: Leetcode 682 Baseball Game
class BaseballGameSolution:
    def calPoints(self, operations: List[str]) -> int:

        #create an empty stack
        kpScr = []

        #iterate through operations list passed by user
        for ops in operations:

        #if ops = "+" push the value of the two prev elements passed
            if ops == "+":
                kpScr.append(kpScr[-1] + kpScr[-2])

        #if ops = "D" push the value of the previous element doubled
            elif ops == "D":
                kpScr.append(kpScr[-1]*2)
              
        #if ops = "C" remove the last element of the stack
            elif ops == "C":
                kpScr.pop()
              
        #if all other if statements are false, user passed an operand, so push the operand to the stack to wait for further instructions
            else:
                kpScr.append(int(ops))
              
        #return sum of all operands
        return sum(kpScr)
