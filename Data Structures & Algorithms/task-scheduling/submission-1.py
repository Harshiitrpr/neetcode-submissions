from collections import deque, Counter
import heapq

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        cooldown = deque([])
        freq = Counter(tasks)
        heap = [[-val, idx] for idx, val in freq.items()]
        heapq.heapify(heap)
        time = 0
        while heap or cooldown:
            time += 1
            while cooldown and cooldown[0][0] <= time:
                exp, freq, task = cooldown.popleft()
                heapq.heappush(heap, [freq, task])
            if heap:
                freq, task = heapq.heappop(heap)
                if freq + 1 < 0:
                    cooldown.append([time + n + 1, freq + 1, task])
        return time


