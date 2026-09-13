class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        seen = [False] * 26
        count = 0
        for ch in sentence.lower():
            if 'a'<= ch <= 'z':
                index = ord(ch) - ord('a')
                if not seen[index]:
                    seen[index] = True
                    count += 1
        return count == 26 
