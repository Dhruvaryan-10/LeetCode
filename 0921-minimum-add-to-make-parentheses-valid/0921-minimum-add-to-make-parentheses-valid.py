class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        stack = []
        count = 0
        for ch in s:
            if ch == '(':
                stack.append('(')
            elif ch == ')':
                if stack:
                    stack.pop()
                else:
                    count += 1
        return len(stack) + count  