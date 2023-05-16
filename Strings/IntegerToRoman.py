#Name: Nick Bear
#Date: 5/16/23
#Assignment: 12. Integer to Roman

class IntegerToRoman:
    def intToRoman(self, num: int) -> str:
        
        #create list that holds definitions of each roman num
        list = [["I", 1], ["IV", 4], ["V", 5], ["IX", 9], ["X", 10], ["XL", 40], ["L", 50], ["XC", 90], ["C", 100], ["CD", 400], ["D", 500], ["CM", 900], ["M", 1000]]

        #empty string to hold our results
        result = ""
        
        #for all [symbols, values] in list, run the statement in reverse
        for symbol, value in reversed(list):
            
            #if num divides value (using integer division) 
            if num // value: 
                
                #let count keep track of how many times it divides
                count = num // value
                
                #let result append the symbol multiplied by the count
                result += (symbol * count)
                
                #update nums to reflect the value accounted for
                num -= value*count
                
        return result
