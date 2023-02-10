class StudentLunchSolution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
      
      #Create a pointer to the top of the sandwich stack
        sandwich = sandwiches[0]

        #while the sandwich at the top of the sandwich stack is in students and there are sandwiches to give
        #Run the following block of code
        while((sandwich in students) and len(sandwiches) > 0):

            #if the student at the top of the queue wants the sandwich at the top of stack
            #pop stack and dequeue queue, giving the student the sandwich and removing both from the lines
            if(students[0] == sandwiches[-1]):
                students.pop(0)
                sandwiches.pop(0)
                
                #check if there are anymore sandwiches in the stack
                #if so, set the sandwich now being tested in the conditionals equal to the top of the stack
                #this is done to update the sandwich being offered to the student queue
                #else the while loop will see the length of sandwiches is 0 and break
                if(len(sandwiches) > 0):
                    sandwich = sandwiches[0]

            #else the current student at the top of the queue does not want the current sandwich at the top of the stack
            #so we create a variable to hold that student and dequeue them
            #after we store the dequeue'd student, we append them to the end of the queue
            else:
                lp = students.pop(0)
                students.append(lp)
                
          #return size of queue
        return len(students)
