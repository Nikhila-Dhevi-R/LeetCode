class Solution:
    def addDigits(self, n: int) -> int:
        
        while n>=10:
            n = sum(int(i) for i in str(n))
        return n
