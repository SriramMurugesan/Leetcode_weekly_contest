import heapq

heap = []

heapq.heappush(heap, 10)
heapq.heappush(heap, 2)
heapq.heappush(heap, 5)
# heap.pop()
print(heap)

x = heapq.heappop(heap)
print(x)
print(heap)
