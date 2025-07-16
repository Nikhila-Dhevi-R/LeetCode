class Solution:
    def addDigits(self, num: int) -> int:
        
        while num>=10:
            sum=0
            temp = num

            while temp>=1 :
                digit = temp %10
                sum+=digit
                temp//=10

            num = sum   
        return num
