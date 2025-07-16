class Solution:
    def mySqrt(self, x: int) -> int:
        if x < 2:
            return x
        else:
            for i in range(0, (x//2)+1):
                if i*i<= x and (i+1)*(i+1)>x:
                    return i
                