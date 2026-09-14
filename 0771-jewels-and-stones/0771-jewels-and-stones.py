class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        seen = set(jewels)
        count = 0
        for stone in stones:
            if stone in seen:
                count += 1
        return count 