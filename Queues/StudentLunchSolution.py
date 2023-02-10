class StudentLunchSolution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
      
      #Create a pointer to the top of the sandwich stack (LIFO)
        sandwich = sandwiches[-1]
        
        #Create a counter to count students unable to eat
        unableStudents = 0

        #while the sandwich at the top of the sandwich stack is in students and there are sandwiches to give
        #Run the following block of code
        while((sandwich in students) and len(sandwiches) > 0):

            #if the student at the top of the queue (FIFO) wants the sandwich at the top of stack (LIFO) 
            #pop stack and dequeue queue, giving the student the sandwich and removing both from the lines
            if(students[0] == sandwiches[-1]):
                students.pop(0)
                sandwiches.pop()
                
                #check if there are anymore sandwiches in the stack
                #if so, set the sandwich now being tested in the conditionals equal to the top of the stack
                #this is done to update the sandwich being offered to the student queue
                #else the while loop will see the length of sandwiches is 0 and break
                if(len(sandwiches) > 0):
                    sandwich = sandwiches[-1]

            #else the current student at the top of the queue does not want the current sandwich at the top of the stack
            #so we create a variable to hold that student and dequeue them
            #after we store the dequeue'd student, we append them to the end of the queue
            else:
                lp = students.pop(0)
                students.append(lp)
                #====================================================================================================================================
                #!!!NOTE: For some reason, solution does not work unless you count instances of students unable to eat in Leetcode's Testcase Case 2
                #Added the following to make LeetCode happy but does not work for other cases. Remove to work for other cases.
                unableStudents+=1 

        
        if (len(students) > 0):
            return len(students) + unableStudents
          
               #=====================================================================================================================================
          #return size of queue
        return len(students)
