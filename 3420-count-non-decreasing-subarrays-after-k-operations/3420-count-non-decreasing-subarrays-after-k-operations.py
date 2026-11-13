from collections import deque

class Solution:
    def countNonDecreasingSubarrays(self, nums: List[int], k: int) -> int:
        n = len(nums)
        ans = 0
        cost = 0
        q = deque()
        r = n - 1
        
        for l in range(n - 1, -1, -1):
            val = nums[l]
            count = 1
            while q and q[0][0] < val:
                prev_val, prev_count = q.popleft()
                cost += (val - prev_val) * prev_count
                count += prev_count
            q.appendleft((val, count))
            
            while cost > k:
                last_val, last_count = q.pop()
                cost -= (last_val - nums[r])
                if last_count > 1:
                    q.append((last_val, last_count - 1))
                r -= 1
                
            ans += r - l + 1
            
        return ans