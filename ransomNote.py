#Name: Nick Bear
#Date: 5/22/23
#Assignment: 383. Ransom Note

class ransomNote:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        #ransomNote needs to be in the set of magazine
        #magazine letters make up our HashMap
        letters = {}

        for l in magazine:
            if l in letters:
                letters[l] += 1
            else:
                letters[l] = 1
          
          #remove count of letters in HM for every occurence in note, if it is less than 0, there are not enough letters
        for k in ransomNote:
            if k in letters:
                letters[k] -= 1
            else:
                letters[k] = -1
                return False

           #Similarly, if there are any values less than 0, then there are not enough letters
        for i in letters:
            if letters[i] < 0:
                return False

        return True
