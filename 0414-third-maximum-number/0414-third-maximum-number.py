class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        nums.sort(reverse=True)
        count = 0
        #if len(nums)>=3:
        for i in range(1,len(nums)):
            if nums[i]!=nums[i-1]:
                count+=1
            if count == 2:
                return nums[i]
        else: 
            return nums[0]
        

