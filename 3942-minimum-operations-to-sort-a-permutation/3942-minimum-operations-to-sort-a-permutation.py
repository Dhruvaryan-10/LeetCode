class Solution:
    def minOperations(self, nums: list[int]) -> int:
        n = len(nums)
        if nums == list(range(n)):
            return 0

        idx0 = nums.index(0)

        # Check if nums is an increasing cyclic shift: [0, 1, 2, ...]
        is_increasing = all(nums[(idx0 + i) % n] == i for i in range(n))
        if is_increasing:
            # Option A: Rotate left idx0 times
            cost_a = idx0
            # Option B: Rev -> Rotate left ((n - idx0) % n) times -> Rev
            cost_b = ((n - idx0) % n) + 2 if idx0 != 0 else 0
            return min(cost_a, cost_b)

        # Check if nums is a decreasing cyclic shift: [0, n-1, n-2, ...]
        is_decreasing = all(nums[(idx0 - i) % n] == i for i in range(n))
        if is_decreasing:
            # Option A: Rotate left (idx0 + 1) % n times -> Rev
            cost_a = ((idx0 + 1) % n) + 1
            # Option B: Rev -> Rotate left (n - 1 - idx0) times
            cost_b = (n - 1 - idx0) + 1
            return min(cost_a, cost_b)

        return -1