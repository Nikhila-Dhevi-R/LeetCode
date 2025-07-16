class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        l = len(s)
        for i in range(0,l):
            if i<l:
                s[i] , s[l-1] = s[l-1],s[i]
                l-=1
            
        #return s 


        