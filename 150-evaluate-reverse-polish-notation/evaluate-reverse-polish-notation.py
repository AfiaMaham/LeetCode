class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for i in range(len(tokens)):
            if tokens[i] in '+-*/':
                val2 = int(stack.pop())
                val1 = int(stack.pop())
                if tokens[i] == '+':
                    stack.append(val1 + val2)
                if tokens[i] == '-':
                    stack.append(val1 - val2)
                if tokens[i] == '*':
                    stack.append(val1 * val2)
                if tokens[i] == '/':
                    stack.append(val1 / val2)
            else:
                stack.append(tokens[i])
        return int(stack[-1])
        