import heapq

class Solution:
    def busiestServers(self, k: int, arrival: list[int], load: list[int]) -> list[int]:
        busy = []
        free_after = list(range(k))
        free_before = []
        requests_count = [0] * k
        
        for i, (time, duration) in enumerate(zip(arrival, load)):
            target = i % k
            
            while busy and busy[0][0] <= time:
                _, server_id = heapq.heappop(busy)
                if server_id >= target:
                    heapq.heappush(free_after, server_id)
                else:
                    heapq.heappush(free_before, server_id)
                    
            if target == 0:
                while free_before:
                    heapq.heappush(free_after, heapq.heappop(free_before))
            else:
                while free_after and free_after[0] < target:
                    heapq.heappush(free_before, heapq.heappop(free_after))
                    
            if free_after:
                assigned = heapq.heappop(free_after)
            elif free_before:
                assigned = heapq.heappop(free_before)
            else:
                continue
                
            requests_count[assigned] += 1
            heapq.heappush(busy, (time + duration, assigned))
            
        max_req = max(requests_count)
        return [i for i, cnt in enumerate(requests_count) if cnt == max_req]