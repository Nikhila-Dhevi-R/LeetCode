class Solution:
    def checkRecord(self, s: str) -> bool:
        countA = 0
        
        for i in s:
            if "LLL" in s:
                return False
            if i == "A":
                countA+=1
            
            
        
        if countA < 2 :
            return True
        else:
            return False
        