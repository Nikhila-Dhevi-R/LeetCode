class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        s_sorted = "".join(sorted(s))
        
        t_sorted = "".join(sorted(t))

        return s_sorted==t_sorted
        '''
        if len(s) == len(t):
            for char in t:
                if char in s:
                    return True
                else:
                    return False
        return False
        '''