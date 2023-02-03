#Name: Nick Bear
#Date: 2/2/2023
#Assignment: Leetcode 155 Min Stack
class MinStack:

    #Create constructor that creates two arrays/stacks 
    #One for general purposes, the other to keep track of minimum element at every operation of the first stack
    def __init__(self):
        self.stack = []
        self.minStack = []

    #Push element to regular stack
    #If minStack exists, set element = min of val passed and last minStack element value, append the results
    def push(self, val: int) -> None:
        self.stack.append(val)
        if (self.minStack):
            val = min(val, self.minStack[-1])
        self.minStack.append(val)

    #Remove the top element of both stacks
    def pop(self) -> None:
        self.stack.pop()
        self.minStack.pop()

    #Return the top element of regular stack
    def top(self) -> int:
        return self.stack[-1]

    #Return the top element of minStack
    def getMin(self) -> int:
        return self.minStack[-1]
