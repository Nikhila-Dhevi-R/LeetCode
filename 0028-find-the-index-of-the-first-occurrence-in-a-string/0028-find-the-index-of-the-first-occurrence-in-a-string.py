class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if len(haystack)<len(needle):
            return -1
        elif len(haystack)>=len(needle):
            for i in range(len(haystack)):
                if(haystack[i : i+len(needle)]) == needle:
                    return i
            return -1
            