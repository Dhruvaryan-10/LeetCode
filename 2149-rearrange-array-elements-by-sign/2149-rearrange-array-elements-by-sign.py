class Solution:
    def rearrangeArray(self, nums: list[int]) -> list[int]:
        positive = []
        negative = []
        for num in nums:
            if num >= 0:
                positive.append(num)
            else:
                negative.append(num)
        result = []
        i = 0
        j = 0
        while i < len(positive) and j < len(negative):
            result.append(positive[i])
            result.append(negative[j])
            i += 1
            j += 1
        while i < len(positive):
            result.append(positive[i])
            i += 1
        while j < len(negative):
            result.append((negative[j]))
            j += 1
        return result 