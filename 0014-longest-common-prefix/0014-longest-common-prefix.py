
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        #def prefix(strs):
            prefix = strs[0]
            for s in strs[1:]:
                while not s.startswith(prefix):
                    prefix = prefix[:-1]
                    if not prefix:
                        return ""
            return prefix
        