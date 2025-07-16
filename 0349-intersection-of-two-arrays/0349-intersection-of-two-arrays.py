class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        '''nums3=[]
        for i in nums1:
            for j in nums2:
                if i==j:
                    nums3.append(i)
        nums3 = set(nums3)        
        return list(nums3)'''
        return list(set(nums1) & set(nums2))


