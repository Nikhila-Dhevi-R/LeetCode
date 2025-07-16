class Solution:
    def climbStairs(self, n: int) -> int:
        if n<=3:
            return n
        else:
            pre=3
            pre1=2
            curr=0
            for i in range(3,n):
                curr = pre + pre1
                pre1=pre
                pre=curr
                
            return curr