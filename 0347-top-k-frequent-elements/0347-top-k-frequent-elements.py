class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        frequency = {}
        for num in nums:
            frequency[num] = frequency.get(num, 0) + 1
        result = sorted(frequency, key = frequency.get ,reverse = True)
        return result[:k]
    