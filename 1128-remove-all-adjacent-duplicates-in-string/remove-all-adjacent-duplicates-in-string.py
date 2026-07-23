class Solution:
    def removeDuplicates(self, s: str) -> str:
        stack = []
        for i in range(len(s)):
            if stack:
                if s[i] == stack[-1]:
                    stack.pop()
                else:
                    stack.append(s[i])
            else:
                stack.append(s[i])
        return ''.join(stack)
            


        