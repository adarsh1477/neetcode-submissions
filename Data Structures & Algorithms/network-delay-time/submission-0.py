from collections import defaultdict
import heapq
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        holder = float('inf')
        min_time = [holder]*(n+1)
        min_time[k] = 0
        min_time[0] = 0
        D = defaultdict(list)



        for u,v,w in times:
            D[u].append((v,w))

        heap = [(0,k)]

        while heap:
            curr_time,node = heapq.heappop(heap)

            for nei,time in D[node]:
                new_time = curr_time+time
                if min_time[nei] > new_time:
                    min_time[nei] = new_time
                    heapq.heappush(heap,(new_time,nei))


        if max(min_time) == float('inf'):
            return -1
        return max(min_time)

