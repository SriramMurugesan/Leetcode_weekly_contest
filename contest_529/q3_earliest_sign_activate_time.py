
import heapq

class Solution:
    def earliestActivation(self, n, edges, requiredSignals):

        # 1. Build adjacency list
        graph = [[] for _ in range(n)]

        for u, v, delay in edges:
            graph[u].append((v, delay))

        # 2. Initialize arrays
        ans = [-1] * n
        count = [0] * n

        # 3. Initialize min heap
        heap = []

        # Node 0 is initially active
        ans[0] = 0

        # Send signals from node 0
        for v, delay in graph[0]:
            heapq.heappush(heap, (delay, 0, v))

        # 4. Process signal events
        while heap:

            # Get earliest arriving signal
            time, u, v = heapq.heappop(heap)

            # Ignore signals to already active nodes
            if ans[v] != -1:
                continue

            # Count this incoming neighbor
            count[v] += 1

            # Check activation requirement
            if count[v] == requiredSignals[v]:

                # Activate the node
                ans[v] = time

                # Send signals to outgoing neighbors
                for next_node, delay in graph[v]:

                    arrival = time + delay

                    heapq.heappush(
                        heap,
                        (arrival, v, next_node)
                    )

        # 5. Return activation times
        return ans
 