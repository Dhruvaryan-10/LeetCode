import sys
sys.setrecursionlimit(300000)

class Solution:
    def palindromePath(self, n: int, edges: list[list[int]], s: str, queries: list[str]) -> list[bool]:
        adj = [[] for _ in range(n)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
            
        LOGN = 18
        up = [[0] * LOGN for _ in range(n)]
        depth = [0] * n
        tin = [0] * n
        tout = [0] * n
        timer = 0
        s_list = list(s)
        mask_val = [1 << (ord(c) - ord('a')) for c in s_list]
        initial_root_mask = [0] * n
        stack = [(0, -1, 0)]
        visited_order = []
        parent = [-1] * n
        order = []
        q = [0]
        parent[0] = 0
        head = 0
        while head < len(q):
            u = q[head]
            head += 1
            for v in adj[u]:
                if v != parent[u]:
                    parent[v] = u
                    depth[v] = depth[u] + 1
                    q.append(v)
                    
        for u in q:
            up[u][0] = parent[u]
            for j in range(1, LOGN):
                up[u][j] = up[up[u][j - 1]][j - 1]
        timer = 1
        call_stack = [(0, 0)]
        it_adj = [iter(adj[i]) for i in range(n)]
        
        tin[0] = timer
        timer += 1
        initial_root_mask[0] = mask_val[0]
        
        while call_stack:
            u = call_stack[-1][0]
            try:
                v = next(it_adj[u])
                if v != parent[u]:
                    tin[v] = timer
                    timer += 1
                    initial_root_mask[v] = initial_root_mask[u] ^ mask_val[v]
                    call_stack.append((v, 0))
            except StopIteration:
                tout[u] = timer - 1
                call_stack.pop()

        def get_lca(u: int, v: int) -> int:
            if depth[u] < depth[v]:
                u, v = v, u
            diff = depth[u] - depth[v]
            for j in range(LOGN):
                if (diff >> j) & 1:
                    u = up[u][j]
            if u == v:
                return u
            for j in range(LOGN - 1, -1, -1):
                if up[u][j] != up[v][j]:
                    u = up[u][j]
                    v = up[v][j]
            return up[u][0]
        bit = [0] * (n + 2)
        
        def bit_xor(idx: int, val: int):
            while idx <= n:
                bit[idx] ^= val
                idx += idx & (-idx)
                
        def bit_query(idx: int) -> int:
            res = 0
            while idx > 0:
                res ^= bit[idx]
                idx -= idx & (-idx)
            return res
        for u in range(n):
            bit_xor(tin[u], mask_val[u])
            bit_xor(tout[u] + 1, mask_val[u])
            
        ans = []
        for q_str in queries:
            parts = q_str.split()
            if parts[0] == "update":
                u = int(parts[1])
                new_char = parts[2]
                old_val = mask_val[u]
                new_val = 1 << (ord(new_char) - ord('a'))
                delta = old_val ^ new_val
                
                if delta != 0:
                    mask_val[u] = new_val
                    bit_xor(tin[u], delta)
                    bit_xor(tout[u] + 1, delta)
                    
            else:
                u = int(parts[1])
                v = int(parts[2])
                lca = get_lca(u, v)
                
                mask_u = bit_query(tin[u])
                mask_v = bit_query(tin[v])
                lca_node_mask = mask_val[lca]
                path_mask = mask_u ^ mask_v ^ lca_node_mask
                ans.append((path_mask & (path_mask - 1)) == 0)
                
        return ans