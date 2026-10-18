
class Solution:
    def numOfWays(self, nums: List[int]) -> int:
        MOD = 10**9 + 7
        n = len(nums)
        comb = [[0] * n for _ in range(n)]
        for i in range(n):
            comb[i][0] = 1
            for j in range(1, i + 1):
                comb[i][j] = (comb[i - 1][j - 1] + comb[i - 1][j]) % MOD

        def count(arr):
            if len(arr) <= 2:
                return 1

            root = arr[0]
            left = [x for x in arr[1:] if x < root]
            right = [x for x in arr[1:] if x > root]

            left_count = count(left)
            right_count = count(right)

            ways_to_interleave = comb[len(left) + len(right)][len(left)]

            return (ways_to_interleave * left_count * right_count) % MOD

        return (count(nums) - 1) % MOD
