class Solution:
    def minInsertions(self, s: str) -> int:
        open_bracket = 0
        insertion = 0
        i = 0
        while i < len(s):
            if s[i] == '(':
                open_bracket += 1
                i += 1
            else:
                if i + 1 < len(s) and s[i + 1] == ')':
                    i += 2
                else:
                    insertion += 1
                    i += 1
                if open_bracket > 0:
                    open_bracket -= 1
                else:
                    insertion += 1
        insertion += open_bracket * 2
        return insertion        