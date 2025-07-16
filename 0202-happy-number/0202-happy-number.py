class Solution:
    def isHappy(self, n: int) -> bool:
            if n==7 :
                return True
        
            while n>=10:
                
                sq=0
                temp = n
                while temp>0:
                    dig = temp%10
                    sq = sq+(dig*dig)
                    temp//= 10 
                
                n = sq
                if n==7 :
                    return True
            return n == 1