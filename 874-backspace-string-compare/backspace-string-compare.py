class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        def func(string):
            stack = []
            for i in string:
                if i == "#":
                    if stack:
                        stack.pop()
                else:
                    stack.append(i)
            return "".join(stack)
        
        if func(s) == func(t):
            return True
        return False