class Solution:
    def intValue(self, roman):
        match roman:
            case 'I':
                return 1
            case 'V':
                return 5
            case 'X':
                return 10
            case 'L':
                return 50
            case 'C':
                return 100
            case 'D':
                return 500
            case 'M':
                return 1000
            case _:
                return 0

    def romanToInt(self, s: str) -> int:
        x = 0
        y = len(s)

        for i in range(y):
            a = self.intValue(s[i])

            if i < y - 1 and a < self.intValue(s[i + 1]):
                x -= a
            else:
                x += a

        return x