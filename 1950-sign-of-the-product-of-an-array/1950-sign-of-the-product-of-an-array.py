class Solution:
    def arraySign(self, nums: List[int]) -> int:
        def signFunc(x):
            if x>0:
                return 1
            elif x<0:
                return -1
            else:
                return 0
        product=1
        for i in nums:
            product*=i
            
        return signFunc(product)
            