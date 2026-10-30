import heapq
from collections import defaultdict
class Solution:
    def shortestPath(self, n: int, edges: list[list[int]], labels: str, k: int) -> int:
        adj = defaultdict(list)
        for u, v, w in edges:
            adj[u].append((v, w))
        dist = {}
        pq = [(0, 0, 1)]
        dist[(0, 1)] = 0
        while pq:
            d, u, cnt = heapq.heappop(pq)
            if u == n - 1:
                return d
            if d > dist.get((u, cnt), float('inf')):
                continue
            for v, w in adj[u]:
                next_cnt = cnt + 1 if labels[v] == labels[u] else 1
                if next_cnt <= k:
                    next_cost = d + w
                    if next_cost < dist.get((v, next_cnt), float('inf')):
                        dist[(v, next_cnt)] = next_cost
                        heapq.heappush(pq, (next_cost, v, next_cnt))
                        
        return -1