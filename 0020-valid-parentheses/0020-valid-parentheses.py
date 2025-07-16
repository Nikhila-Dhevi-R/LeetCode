class Solution:
    def isValid(self, s: str) -> bool:
        matching_dict = {'(': ')', '{': '}', '[': ']'}

        stack = []

        for c in s:
            if c in ['(', '{', '[']:
                stack.append(c)
            else:
                if not stack:
                    return False
                else:
                    if matching_dict[stack[-1]] == c:
                        stack.pop()
                    else:
                        return False

        return not stack