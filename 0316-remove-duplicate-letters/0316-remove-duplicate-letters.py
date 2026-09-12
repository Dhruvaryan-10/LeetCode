class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        freq ={}
        for ch in s:
            freq[ch] = freq.get(ch, 0) + 1
        seen = set()
        stack =[]
        for ch in s:
            freq[ch] -= 1
            if ch in seen:
                continue
            while stack and stack[-1] > ch and freq[stack[-1]] > 0:
                removed = stack.pop()
                seen.remove(removed)
            stack.append(ch)
            seen.add(ch)
        return "".join(stack)