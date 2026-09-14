class Solution:
    def minSteps(self, s: str, t: str) -> int:
        freq = [0] * 26
        for ch in s:
            freq[ord(ch) - ord('a')] += 1
        for ch in t:
            freq[ord(ch) - ord('a')] -= 1
        steps = 0

        for count in freq:
            if count > 0:
                steps += count
        return steps