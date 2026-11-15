class Solution:
    def numOfSubarrays(self, arr: list[int]) -> int:
        MOD = 1_000_000_007
        odd = 0
        even = 1
        prefix_parity = 0
        ans = 0
        
        for num in arr:
            prefix_parity ^= (num & 1)
            if prefix_parity:
                ans = (ans + even) % MOD
                odd += 1
            else:
                ans = (ans + odd) % MOD
                even += 1
                
        return ans