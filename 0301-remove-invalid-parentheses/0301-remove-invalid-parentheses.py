class Solution:
    def removeInvalidParentheses(self, s: str) -> list[str]:
        def is_valid(s):
            balance = 0
            for ch in s:
                if ch == '(':
                    balance += 1
                elif ch == ')':
                    balance -= 1
                    if balance < 0:
                        return False
            return balance == 0
        level = {s}
        while True:
            result = []
            for string in level:
                if is_valid(string):
                    result.append(string)
            if result:
                return result 
            new_level = set()
            for string in level:
                for i in range(len(string)):
                    if string[i] == '(' or string[i] == ')':
                        new_string = string[:i] + string[i+1:]
                        new_level.add(new_string)
            level = new_level